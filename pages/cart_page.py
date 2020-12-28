from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class CartPage(BasePage):

    # locators
    CHECKOUT_BTN = (By.XPATH, "//button[@class='Button MiniBag-continueButton notranslate'][1]")
    CART_ITEMS = (By.CLASS_NAME, 'OrderProducts-product')
    REMOVE_ITEM_BTNS = (By.CSS_SELECTOR, '.OrderProducts-deleteText.notranslate')
    PROMO_FIELD = (By.ID, 'promotionCode-text')
    APPLY_PROMO_BTN = (By.XPATH,"//button[contains(text(),'Apply')]")
    SHIPPING_SELECT = (By.ID, "miniBagDeliveryType")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[contains(text(),'Continue shopping')]")


    def __init__(self, driver):
        super().__init__(driver)

    def goto(self):
        self.goto_cart()

    def goto_checkout_page(self):
        self.driver.element_click(self.CHECKOUT_BTN)

    def remove_item_from_cart(self):
        CONFIRM_BTN = (By.XPATH, "//button[@class='Button OrderProducts-deleteButton']")
        self.driver.element_click(self.REMOVE_ITEM_BTNS)
        self.driver.element_click(CONFIRM_BTN)

    def clear_cart(self):
        items = self.driver.get_elements_list(self.REMOVE_ITEM_BTNS)
        for i in range(len(items)):
            self.remove_item_from_cart()

        self.driver.element_click(self.CONTINUE_SHOPPING_BTN)

    def verify_empty_cart(self):
        return not self.driver.is_element_present(self.CART_ITEMS)
