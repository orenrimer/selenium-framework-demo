import pytest
from pages.login_page import LoginPage
from utilities.generic_utils import generate_random_password, generate_random_email



pytestmark = [pytest.mark.smoke, pytest.mark.login]

class TestLogin:

    @pytest.fixture()
    def setup(self, driver_setup):
        self.login_page = LoginPage(driver_setup)
        self.login_page.goto()
        yield
        self.login_page.goto_home_page()

    @pytest.mark.order(1)
    @pytest.mark.tcid2
    def test_login_invalid_email(self, setup):
        email = generate_random_email()
        self.login_page.login(email=email)
        assert self.login_page.verify_login_failed()
        if AssertionError:
            self.login_page.driver.take_screenshot(name="test_login_invalid_email")

    @pytest.mark.order(2)
    @pytest.mark.tcid3
    def test_login_invalid_password(self, setup):
        password = generate_random_password()
        self.login_page.login(password=password)
        assert self.login_page.verify_login_failed()
        if AssertionError:
            self.login_page.driver.take_screenshot(name="test_login_invalid_password")

    @pytest.mark.order(3)
    @pytest.mark.tcid4
    def test_login_valid_user(self, setup):
        self.login_page.login()
        assert self.login_page.verify_logged_in()
        if AssertionError:
            self.login_page.driver.take_screenshot(name="test_login_valid_user")
