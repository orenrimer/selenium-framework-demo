import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.results_page import ResultsPage
from pages.wishlist_page import WishlistPage

pytestmark = [pytest.mark.smoke, pytest.mark.productpage]


class TestProductPage:

    @pytest.fixture()
    def setup(self, driver_setup):
        self.results_page = ResultsPage(driver_setup)
        self.product_page = ProductPage(driver_setup)
        self.login_page = LoginPage(driver_setup)
        self.wish = WishlistPage(driver_setup)
        self.product = "jeans"

    @pytest.mark.tcid15
    def test_add_product_to_cart_as_user(self, setup):
        self.login_page.goto()
        self.login_page.login()
        self.results_page.goto_product(self.product)
        self.product_page.add_to_bag(select_type="dropdown")
        assert self.product_page.verify_added_to_bag()
        if AssertionError:
            self.login_page.driver.take_screenshot(name="test_add_product_to_cart_as_user")

    @pytest.mark.tcid16
    def test_add_product_to_wishlist_as_user(self, setup):
        self.login_page.goto()
        self.login_page.login()
        self.results_page.goto_product(self.product)
        product_name = self.product_page.get_product_title()
        self.product_page.add_to_wishlist(select_type="dropdown")
        assert self.wish.verify_product_in_wishlist(product_name)
        if AssertionError:
            self.login_page.driver.take_screenshot(name="test_add_product_to_wishlist_as_user")

    @pytest.mark.tcid17
    def test_add_product_to_cart_as_guest(self, setup):
        self.results_page.goto_product(self.product)
        self.product_page.add_to_bag(select_type="dropdown")
        assert self.product_page.verify_added_to_bag()
        if AssertionError:
            self.login_page.driver.take_screenshot(name="test_add_product_to_wishlist_as_user")

    @pytest.mark.tcid18
    def test_guest_must_login_to_wishlist_product(self, setup):
        self.results_page.goto_product(self.product)
        self.product_page.add_to_wishlist(select_type="dropdown")
        assert self.product_page.verify_login_prompt()
        if AssertionError:
            self.login_page.driver.take_screenshot(name="test_guest_must_login_to_wishlist_product")
