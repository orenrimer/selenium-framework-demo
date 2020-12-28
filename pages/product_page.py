import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    
    # locators
    PRODUCT_TITLE = (By.XPATH, "//h1[contains(@class,'ProductDetail-title')]")
    AVAILABLE_SIZES = (By.CLASS_NAME, 'ProductSizes-item')
    SIZE_SELECT = (By.ID, 'productSizes')
    COLOR_PICKER = (By.XPATH, "//div[@class='SwatchList-cell']")
    WISHLIST_BTN = (By.XPATH, "//button[@class='WishlistButton notranslate WishlistButton--pdp']")
    ADD_TO_BAG_BTN = (By.XPATH, "//div[contains(@class,'ProductDetail-secondaryButtonGroup')]//div//button")

    
    def __init__(self, driver):
        super().__init__(driver)

    def select_available_size(self, size=None, select_type=None):
        if not select_type: return
        if select_type == "dropdown":
            options = self.driver.get_elements_list((By.XPATH, "//select[@id='productSizes']/option"))
            available_options = [i for i in options if
                                 not self.driver.element_has_attribute(element=i, attribute="disabled")]
        elif select_type == "buttons":
            available_options = self.driver.get_elements_list(self.AVAILABLE_SIZES)
        else:
            raise Exception(f"Parameter 'select_type' is invalid:: {select_type}")

        if not available_options: return
        if not size:
            size = random.choice(available_options)
            self.driver.element_click(element=size)
        else:
            for option in available_options:
                if size.upper() in option.text:
                    self.driver.element_click(element=option)
                    return
            raise Exception(f"Size is invalid or unavailable:: {size}")

    def click_add_to_wishlist(self):
        self.driver.element_click(self.WISHLIST_BTN)

    def add_to_wishlist(self, size=None, color=None, select_type=None):
        self.select_available_size(size=size, select_type=select_type)
        self.click_add_to_wishlist()

    def click_add_to_bag(self):
        self.driver.element_click(self.ADD_TO_BAG_BTN)

    def add_to_bag(self, size=None, color=None, select_type=None):
        self.select_available_size(size=size, select_type=select_type)
        self.click_add_to_bag()
     
    def get_product_title(self):
        return self.driver.element_get_text(self.PRODUCT_TITLE)

    def verify_added_to_bag(self):
        conformation_msg = (By.XPATH, "//div[contains(@class,'InlineConfirm-label')]")
        return self.driver.is_element_present(conformation_msg)

    def verify_login_prompt(self):
        login_window = (By.XPATH, "//div[@class ='WishlistLoginModal-header']")
        return self.driver.is_element_present(login_window)
