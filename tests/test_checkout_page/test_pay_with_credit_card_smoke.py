import os

import pytest
from ddt import data, unpack

from pages.cart_page import CartPage
from pages.checkout_pages.delivery_page import DeliveryPage
from pages.checkout_pages.payment_page import PaymentPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.results_page import ResultsPage
from utilities.read_data import getCSVData



pytestmark = [pytest.mark.smoke, pytest.mark.checkout]

@ddt
class TestPayWithCreditCard:

    root = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(root, "..", "test_data", "CCRecords.csv")

    @pytest.fixture(scope="class")
    def setup(self, driver_setup):
        self.login_page = LoginPage(driver_setup)
        self.results_page = ResultsPage(driver_setup)
        self.product_page = ProductPage(driver_setup)
        self.cart = CartPage(driver_setup)
        self.payment_page = PaymentPage(driver_setup)
        self.delivery_page = DeliveryPage(driver_setup)
        self.product = "jeans"


    @pytest.fixture(scope="class")
    def prerequisites(self, setup):
        self.login_page.goto()
        self.login_page.login()
        self.results_page.goto_product(self.product)
        self.product_page.add_to_bag(select_type="dropdown")
        self.cart.goto()
        self.cart.goto_checkout_page()
        self.delivery_page.enter_full_delivery_details()


    @data(*getCSVData(data_path))
    @unpack
    @pytest.mark.tcid30
    def test_pay_with_valid_card(self, setup, preconditions, ccNum, ccExp, ccCVV):
        self.payment_page.place_order(payment_options="card", curd_num=ccNum,
                                      expiry_date=ccExp, cvv=ccCVV)
        assert self.payment_page.verify_successful_payment()
        if AssertionError:
            self.delivery_page.driver.take_screenshot(name="test_pay_with_valid_card")
