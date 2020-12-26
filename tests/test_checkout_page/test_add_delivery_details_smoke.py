import os
import pytest
from ddt import data, unpack
from pages.cart_page import CartPage
from pages.checkout_pages.delivery_page import DeliveryPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.results_page import ResultsPage
from utilities.read_data import getCSVData

pytestmark = [pytest.mark.smoke, pytest.mark.checkout, pytest.mark.deliverypage]

class TestAddDeliveryAddress:

    root = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(root, "..", "test_data", "AddressRecords.csv")

    @pytest.fixture(scope="class")
    def setup(self, driver_setup):
        self.login_page = LoginPage(driver_setup)
        self.results_page = ResultsPage(driver_setup)
        self.product_page = ProductPage(driver_setup)
        self.cart = CartPage(driver_setup)
        self.delivery_page = DeliveryPage(driver_setup)
        self.product = "jeans"


    @pytest.fixture(scope="class")
    def preconditions(self, setup):
        self.login_page.goto()
        self.login_page.login()
        self.results_page.goto_product(self.product)
        self.product_page.add_to_bag(select_type="dropdown")
        self.cart.goto()
        self.cart.goto_checkout_page()


    @data(*getCSVData(data_path))
    @unpack
    @pytest.mark.tcid25
    def test_add_valid_delivery_details(self,setup, preconditions, PhoneNum, Postcode, fullAddress):
        self.delivery_page.enter_full_delivery_details(phone=PhoneNum, postcode=Postcode, full_address=fullAddress)
        assert self.delivery_page.verify_valid_delivery_details()
        if AssertionError:
            self.delivery_page.driver.take_screenshot(name="test_add_valid_delivery_details")