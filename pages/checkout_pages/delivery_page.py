import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities import generic_utils



class DeliveryPage(BasePage):

    # locators
    DELIVERY_OPTION_HOME = (By.CSS_SELECTOR, '.DeliveryOption--home')
    DELIVERY_OPTION_PICKUP = (By.CSS_SELECTOR, '.DeliveryOption--store')
    DELIVERY_OPTION_PS = (By.CSS_SELECTOR, '.DeliveryOption--parcelshop')
    FIRST_NAME_FIELD = (By.ID, "firstName-text")
    LAST_NAME_FIELD = (By.ID, "lastName-text")
    PHONE_FIELD = (By.ID, "telephone-tel")
    COUNTRY_SELECT = (By.ID, "country")
    POSTCODE_FIELD = (By.ID, "postcode-text")
    MANUALLY_ENTER_ADDRESS_BTN = (By.CSS_SELECTOR, ".FindAddressV1-link")
    HOUSE_NUMBER_FIELD = (By.ID, "houseNumber-text")
    FIND_ADDRESS_BTN = (By.XPATH, "//button[contains(text(),'Find Address')]")
    ADDRESS_FIELD = (By.ID, "address1-text")
    CITY_FIELD = (By.ID, "city-text")
    DELIVERY_METHOD_STANDARD = (By.ID, "delivery-method-home_standard")
    DELIVERY_METHOD_EXPRESS = (By.ID, "delivery-method-home_express")
    PROCEED_BTN = (By.XPATH, "//button[contains(text(),'Proceed')]")
    BACK_TO_SHOPPING_BTN = (By.CSS_SELECTOR, "div.CheckoutCTA")


    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.driver.element_send_keys(first_name, self.FIRST_NAME_FIELD)

    def enter_last_name(self, last_name):
        self.driver.element_send_keys(last_name, self.LAST_NAME_FIELD)

    def enter_phone_number(self, phone):
        self.driver.element_send_keys(phone, self.PHONE_FIELD)

    def select_delivery_country(self, delivery_country):
        if delivery_country:
            select_country = self.driver.element_select(self.COUNTRY_SELECT)
            select_country.select_by_value(delivery_country.title())

    def enter_postcode(self, postcode):
        self.driver.element_send_keys(postcode, self.POSTCODE_FIELD)


    def choose_delivery_option(self, delivery_option):
        if delivery_option == "home":
            self.driver.element_click(self.DELIVERY_OPTION_HOME)
        elif delivery_option == "pickup":
            self.driver.element_click(self.DELIVERY_OPTION_PICKUP)
        elif delivery_option == "parcel shop":
            self.driver.element_click(self.DELIVERY_OPTION_PS)
        else:
            raise Exception(f"Invalid parameter 'delivery_option':: {delivery_option} ")

    def enter_delivery_address(self, phone, postcode, full_address, first_name=None, last_name=None):
        self.driver.element_click(self.MANUALLY_ENTER_ADDRESS_BTN)

        if not first_name: first_name = generic_utils.generate_random_string()
        self.enter_first_name(first_name)
        
        if not last_name: last_name = generic_utils.generate_random_string()
        self.enter_last_name(last_name)

        self.enter_phone_number(phone)

        address, city = full_address.split(',')
        self.driver.element_send_keys(data=address, locator=self.ADDRESS_FIELD)
        self.enter_postcode(postcode)
        self.driver.element_send_keys(data=city, locator=self.CITY_FIELD)


    def choose_delivery_type(self, delivery_type):
        if delivery_type == "standard":
            self.driver.element_click(self.DELIVERY_METHOD_STANDARD)
        elif delivery_type == "express":
            self.driver.element_click(self.DELIVERY_METHOD_EXPRESS)
        else:
            raise Exception(f"Invalid parameter 'delivery_type':: {delivery_type} ")


    def enter_full_delivery_details(self, phone, postcode, full_address, first_name=None, last_name=None, delivery_option="home", delivery_type='standard'):
        self.choose_delivery_option(delivery_option)
        self.enter_delivery_address(first_name=first_name, last_name=last_name, phone=phone, postcode=postcode, full_address=full_address)
        self.choose_delivery_type(delivery_type)
        self.driver.scroll(self.PROCEED_BTN)
        self.driver.element_click(self.PROCEED_BTN)

    def go_back_to_home_page(self):
        self.driver.element_click(self.BACK_TO_SHOPPING_BTN)


    def verify_valid_delivery_details(self):
        return self.verify_page_title_contains('Billing Options')
