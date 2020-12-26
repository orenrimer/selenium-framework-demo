import pytest

from pages.sign_up_page import SignUpPage
from src import user_info

pytestmark = [pytest.mark.smoke, pytest.mark.signup]


@pytest.fixture()
def join_page(driver_setup):
    join_page = SignUpPage(driver_setup)
    join_page.goto()
    return join_page

@pytest.mark.tcid1
def test_create_valid_user(join_page):
    join_page = join_page
    join_page.sign_up()
    assert join_page.verify_successful_signup()
    if AssertionError:
        join_page.driver.take_screenshot(name="test_create_valid_user")

@pytest.mark.tcid9
def test_fails_create_user_with_existing_email(join_page):
    join_page = join_page
    join_page.sign_up(email=user_info.EMAIL)
    assert join_page.verify_invalid_signup()
    if AssertionError:
        join_page.driver.take_screenshot(name="test_fails_create_user_with_existing_email")