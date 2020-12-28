import os
import time
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.custom_logger import custom_logger


class CustomDriver:


    def __init__(self, driver):
        self.driver = driver
        self.logger = custom_logger()

    def get_element(self, locator):
        try:
            element = self.element_wait(locator)
            self.logger.info(f"Found element:: {locator}")
            return element
        except NoSuchElementException:
            self.logger.error(f"Can't find element:: {locator}")

    def get_elements_list(self, locator):
        try:
            by, value = locator
            elements = self.driver.find_elements(by, value)
            self.logger.info(f"Found elements:: {locator}")
            return elements
        except NoSuchElementException:
            self.logger.error(f"Can't find elements:: {locator}")

    def is_element_present(self, locator):
        elements = self.get_elements_list(locator)
        if len(elements) > 0:
            self.logger.info(f"Element is present in the page:: {locator}")
            return True
        else:
            self.logger.error(f"Element not present in the page:: {locator}")
            return False

    def is_element_displayed(self, locator="", element=None):
        if locator:
            element = self.get_element(locator)
        return element.is_displayed()

    def element_click(self, locator="", element=None):
        try:
            if locator:
                element = self.get_element(locator)

            max_tries = 3
            try_num = 0
            while try_num < max_tries:
                try:
                    element.click()
                    self.logger.info(f"Clicked on element:: {locator}")
                    break
                except Exception as e:
                    try_num += 1
            else:
                raise Exception(f"cant click on elements:: {locator} after {max_tries} tries")
        except ElementNotInteractableException:
            self.logger.error(f"Can't click on element:: {locator}")
            
    def element_clear(self, locator="", element=None):
        try:
            if locator:
                element = self.get_element(locator)
            element.clear()
            self.logger.info(f"Cleared element:: {locator}")
        except ElementNotInteractableException:
            self.logger.error(f"Can't clear element:: {locator}")

    def element_send_keys(self, data, locator="", element=None):
        try:
            if locator:
                element = self.get_element(locator)
            self.element_clear(element=element)
            element.send_keys(data)
            self.logger.info(f"Typed {data} in element:: {locator}")
        except ElementNotInteractableException:
            self.logger.error(f"Can't type in element:: {locator}")

    def element_select(self, locator="", element=None):
        try:
            if locator:
                element = self.get_element(locator)
                self.logger.info(f"Selected element:: {locator}")
            return Select(element)
        except ElementNotInteractableException:
            self.logger.error(f"Can't select element:: {locator}")

    def element_get_text(self, locator="", element=None):
        try:
            if locator:
                element = self.get_element(locator)
            self.logger.info(f"Got text from element:: {locator}")
            return element.text
        except ElementNotInteractableException:
            self.logger.error(f"Can't get text from element:: {locator}")

    def element_has_attribute(self, attribute, locator="", element=None):
        try:
            if locator:
                element = self.get_element(locator)
            self.logger.info(f"Got attribute from element:: {locator}")
            res = element.get_attribute(attribute)
            if res: return True
            else:
                return False
        except ElementNotInteractableException:
            self.logger.error(f"Can't get attribute from element:: {locator}")

    def element_get_attribute(self, attribute, locator="", element=None):
        try:
            if locator:
                element = self.get_element(locator)
            self.logger.info(f"Got attribute from element:: {locator}")
            return element.get_attribute(attribute)
        except ElementNotInteractableException:
            self.logger.error(f"Can't get attribute from element:: {locator}")

    def take_screenshot(self, name=""):
        root = os.path.dirname(os.path.dirname(__file__))
        screenshots_path = os.path.join(root, "screenshots")
        file_name = name + "_" + str(round(time.time() * 1000)) + ".png"
        try:
            full_path = os.path.join(screenshots_path, file_name)
            self.driver.save_screenshot(full_path)
            self.logger.info(f"Saved screenshot in path:: {full_path}")
        except Exception as e:
            self.logger.error(f"Can't save screenshot in path:: {screenshots_path}, error:{e}")

    def element_wait(self, locator, wait_time=20, poll_freq=0.5):
        try:
            wait = WebDriverWait(self.driver, timeout=wait_time, poll_frequency=poll_freq, ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ])
            by, value = locator
            element = wait.until(EC.presence_of_element_located((by, value)), EC.element_to_be_clickable((by, value)))
            return element
        except ElementNotInteractableException:
            self.logger.error(f"Element doesn't exist in page :: {locator}")

    def wait_for_url(self, wait_time=20, poll_freq=0.5):
        try:
            wait = WebDriverWait(self.driver, timeout=wait_time, poll_frequency=poll_freq)
            current_url = self.get_url()
            wait.until(EC.url_changes(current_url))
        except Exception as e:
            self.logger.error(f"Couldn't wait for page url to change:: error {e}")

    def wait_for_invisibility_of_element(self, locator='', element=None, wait_time=20, poll_freq=0.5):
        try:
            wait = WebDriverWait(self.driver, timeout=wait_time, poll_frequency=poll_freq, ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ])
            if locator:
                element = self.get_element(locator=locator)
            wait.until(EC.invisibility_of_element(element))
        except Exception as e:
            self.logger.error(f"Element doesn't exist in page:: error {e}")

    def switch_frame(self, index="", name="", frame_id=None):
        try:
            if index:
                self.driver.switch_to.frame(index)
                self.logger.info(f"Switched to frame :: number {index} ")
            if name:
                self.driver.switch_to.frame(name)
                self.logger.info(f"Switched to frame :: name {name}")
            if frame_id is not None:
                self.driver.frame(frame_id)
                self.logger.info(f"Switched to frame :: id {id}")
        except Exception as e:
            self.logger.error(f"Can't switch to frame:: error {e}")

    def switch_default_content(self):
        try:
            self.driver.switch_to.default_content()
            self.logger.info("Switched back to default content")
        except Exception as e:
            self.logger.error(f"Can't switch back to default content:: error {e}")

    def scroll(self, locator="", element=None):
        try:
            if locator:
                element = self.get_element(locator)
            if element is None:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);", element)
                self.driver.execute_script("window.scrollBy(0, -150);")
                self.logger.info("Scrolled element into view")
        except Exception as e:
            self.logger.error(f"Can't scroll element into view:: error {e}")

    def get_title(self):
        try:
            title = self.driver.title
            self.logger.info(f"Got page title:: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Can't get page title:: error {e}")

    def get_url(self):
        try:
            url = self.driver.current_url
            self.logger.info(f"Got page url:: {url}")
            return url
        except Exception as e:
            self.logger.error(f"Can't get page url:: error {e}")

    def refresh_page(self):
        try:
            self.driver.refresh()
            self.logger.info("Refreshed page")
        except Exception as e:
            self.logger.error(f"Can't refresh page:: error{e}")

    def navigate_previous_window(self):
        try:
            self.driver.execute_script("window.history.go(-1);")
            self.logger.info("Navigated to previous window")
        except Exception as e:
            self.logger.error(f"Can't navigate to previous window :: error {e}")

    def navigate_next_window(self):
        try:
            self.driver.execute_script("window.history.go(1);")
            self.logger.info("Navigated to next window")
        except Exception as e:
            self.logger.error(f"Can't navigate to next window:: error {e}")

    def execute_script(self, script, element=None):
        if element:
            self.driver.execute_script(script, element)
        else:
            self.driver.execute_script(script)
        self.logger.info(f"Executing JavaScript:: {script}")
