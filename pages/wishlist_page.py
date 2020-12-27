from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WishlistPage(BasePage):

    # locators
    ADD_TO_BAG_BTN = (By.XPATH, "//button[@class='Button WishlistItem-button notranslate']")
    ITEM_TITLE = (By.XPATH, "//p[@class='WishlistItem-titleText']")
    SIZE_SELECT = (By.ID, "Size selection")
    REMOVE_ITEM = (By.XPATH, "//button[@class='WishlistItem-remove']")

    def __init__(self, driver):
        super().__init__(driver)

    def goto(self):
        self.goto_wishlist()

    def verify_product_in_wishlist(self, product_name):
        self.goto()
        titles = self.driver.get_elements_list(self.ITEM_TITLE)
        for title in titles:
            if product_name == title.text:
                return True
        return False
