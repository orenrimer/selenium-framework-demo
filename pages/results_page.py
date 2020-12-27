import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResultsPage(BasePage):
    
    # locators
    PRODUCTS_LINK = (By.XPATH, "//a[@class='Product-nameLink']")
    SORT_SELECT = (By.ID, 'sortSelector')
    PRODUCTS_SEARCH_RES = (By.XPATH, "//span[@class='PlpHeader-title']")

    def __init__(self, driver):
        super().__init__(driver)

    def sort_results(self, by=''):
        _options = (By.XPATH, "//select[@name='sortSelector']//option")
        options = self.driver.get_elements_list(_options)
        options = list(map(lambda x: self.driver.element_get_attribute('value', element=x), options))
        if not by:
            by = random.choice(options)

        if by.title() in options:
            sort_select = self.driver.element_select(self.SORT_SELECT)
            sort_select.select_by_value(by.title())
        else:
            self.driver.logger.error(f"Unsupported sort option:: {by}")

    def verify_sorted(self, by):
        return \
            self.driver.element_get_attribute('aria-activedescendant', self.SORT_SELECT) == by.title()

    def verify_search_result(self, product_name):
        return self.driver.element_get_text(self.PRODUCTS_SEARCH_RES) == product_name.title()

    def select_random_product(self):
        products_list = self.driver.get_elements_list(self.PRODUCTS_LINK)
        product = products_list[random.randint(0, len(products_list)-1)]
        self.driver.element_click(element=product)

    def goto_product(self, product_name):
        self.search(product_name)
        assert self.verify_search_result(product_name), f"product name doesn't match search results"
        self.select_random_product()
