from pages.components import header
from utilities.driver_wrapper import CustomDriver


class BasePage:

    def __init__(self, driver):
        self.driver = CustomDriver(driver)
        self.header = header

    def verify_page_title(self, title_to_verify):
        actual_title = self.driver.get_title()
        return title_to_verify == actual_title

    def verify_page_title_contains(self, title_to_verify):
        actual_title = self.driver.get_title()
        return title_to_verify in actual_title

    def search(self, product_name):
        self.driver.element_send_keys(product_name, self.header.SEARCH_BAR)
        self.driver.element_click(self.header.SEARCH_BTN)

    def goto_account(self):
        self.driver.element_click(self.header.ACCOUNT_BTN)

    def goto_login_page(self):
        self.driver.element_click(self.header.ACCOUNT_BTN)

    def goto_sign_up_page(self):
        self.driver.element_click(self.header.ACCOUNT_BTN)

    def goto_home_page(self):
        self.driver.element_click(self.header.HOME_LINK)

    def goto_cart(self):
        self.driver.element_click(self.header.CART_LINK)

    def goto_wishlist(self):
        self.driver.element_click(self.header.WISHLIST_LINK)

    def sign_out(self):
        self.driver.element_click(self.header.ACCOUNT_BTN)
        self.driver.element_click(self.header.SIGN_OUT_LINK)