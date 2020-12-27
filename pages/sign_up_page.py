from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities import generic_utils


class SignUpPage(BasePage):

    # locators
    EMAIL_FIELD = (By.ID, "Register-email")
    PASSWORD_FIELD = (By.ID, "Register-password")
    JOIN_BTN = (By.XPATH, "//button[contains(text(),'CREATE AN ACCOUNT')]")

    
    def __init__(self, driver):
        super().__init__(driver)

    def goto(self):
        self.goto_sign_up_page()

    def enter_email(self, email):
        self.driver.element_send_keys(email, self.EMAIL_FIELD)

    def enter_password(self, password):
        self.driver.element_send_keys(password, self.PASSWORD_FIELD)

    def sign_up(self, email=None, password=None):
        if not email: email = generic_utils.generate_random_email()
        self.enter_email(email)

        if not password: password = generic_utils.generate_random_password()
        self.enter_password(password)

        self.driver.element_click(self.JOIN_BTN)

    def verify_successful_signup(self):
        return self.driver.is_element_present(self.header.SIGN_OUT_LINK)

    def verify_invalid_signup(self):
        INVALID_SIGNUP_MSG = (By.XPATH, "//p[contains(text(),'Please use a different email address and try again.')]")
        return self.driver.is_element_present(INVALID_SIGNUP_MSG)
