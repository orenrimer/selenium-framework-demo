import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage

pytestmark = [pytest.mark.smoke, pytest.mark.cart]


@pytest.fixture(scope='module')
def setup(driver_setup):
    cart = CartPage(driver_setup)
    login_page = LoginPage(driver_setup)
    login_page.goto()
    login_page.login()
    return cart

@pytest.mark.tcid22
def test_clear_cart(setup):
    cart = setup
    cart.goto()
    cart.clear_cart()
    assert cart.verify_empty_cart()
    if AssertionError:
        cart.driver.take_screenshot(name="test_clear_cart")