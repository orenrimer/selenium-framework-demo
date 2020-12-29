import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaymentPage(BasePage):

    # locators
    CHANGE_ADDRESS_BTN = (By.XPATH, "//button[contains(text(),'Change')]")
    SAME_AS_DELIVERY_CHECKBOX = (By.ID, "deliveryAsBilling-checkbox")
    PAYMENT_OPTIONS_BTN = (By.XPATH, "//button[@class='PaymentMethodOption-button'][@value='{0}']")
    SAVE_PAYMENT_DETAILS_CHECKBOX = (By.ID, 'SavePaymentDetails-checkbox')
    TOTAL_PRICE = (By.XPATH, "//div[contains(@class, 'SimpleTotals-total')]//span[@class='SimpleTotals-groupRight'][1]")
    PAY_BTN = (By.XPATH, "//button[contains(@class, 'Button PaymentBtnWithTC-paynow')]")
    CARD_NUM_FIELD = (By.ID, "cardNumber-tel")
    SELECT_EXPIRY_MONTH = (By.ID, "expiryMonth")
    SELECT_EXPIRY_YEAR = (By.ID, "expiryYear")
    CVV_FIELD = (By.ID, "cvv-tel")


    def __init__(self, driver):
        super().__init__(driver)

    def choose_payment_options(self, payment_option):
        payment_option = payment_option.lower()
        if payment_option == "card":
            self.PAYMENT_OPTIONS_BTN[1].format('CARD')
            self.driver.element_click(self.PAYMENT_OPTIONS_BTN)
        elif payment_option == "paypal":
            self.PAYMENT_OPTIONS_BTN[1].format('PYPAL')
            self.driver.element_click(self.PAYMENT_OPTIONS_BTN)
        elif payment_option == "account card":
            self.PAYMENT_OPTIONS_BTN[1].format('ACCNT')
            self.driver.element_click(self.PAYMENT_OPTIONS_BTN)
        elif payment_option == "klrna":
            self.PAYMENT_OPTIONS_BTN[1].format('KLRNA')
            self.driver.element_click(self.PAYMENT_OPTIONS_BTN)
        elif payment_option == "clearpay":
            self.PAYMENT_OPTIONS_BTN[1].format('CLRPY')
            self.driver.element_click(self.PAYMENT_OPTIONS_BTN)
        else:
            raise Exception(f"Invalid parameter 'payment_option':: {payment_option}. "
                            f"expected 'card', 'paypal, 'account card', 'klrna' or 'clearpay'.")

    def enter_card_num(self, card_num):
        self.driver.element_send_keys(card_num, self.CARD_NUM_FIELD)

    def enter_card_cvv(self, cvv):
        self.driver.element_send_keys(cvv, self.CVV_FIELD)

    def select_card_exp_date(self, expiry_date):
        expiry_month, expiry_year = int(expiry_date.split('/'))
        expiry_month = int(expiry_month)
        expiry_year = int(expiry_year)
        
        if 1 <= expiry_month <= 12:
            select_exp_month = self.driver.element_select(self.SELECT_EXPIRY_MONTH)
            select_exp_month.select_by_index(expiry_month-1)
        else:
            raise Exception(f"Invalid parameter 'expiry_month':: {str(expiry_month)}, must be an integer between 1 and 12.")

        now = datetime.datetime.now()
        curr_year = now.year
        if expiry_year >= curr_year:
            select_exp_month = self.driver.element_select(self.SELECT_EXPIRY_MONTH)
            select_exp_month.select_by_index(expiry_month-1)
        else:
            raise Exception(f"Invalid parameter 'expiry_year':: {str(expiry_month)}, card id expired.")

    def fill_card_details(self, curd_num, expiry_date, cvv):
        self.choose_payment_options(payment_option='card')
        self.enter_card_num(curd_num)
        self.select_card_exp_date(expiry_date)
        self.enter_card_cvv(cvv)

    def place_order(self, payment_options, curd_num, expiry_date, cvv):
        self.choose_payment_options(payment_options)
        if payment_options == "card" or payment_options == 'account card':
            self.fill_card_details(curd_num, expiry_date, cvv)
        self.driver.element_click(self.PAY_BTN)

    def verify_successful_payment(self):
        return self.verify_page_title_contains('Thank You')

    def verify_invalid_card_details(self):
        return self.driver.element_get_attribute('aria-disabled', self.PAY_BTN) == "true"
