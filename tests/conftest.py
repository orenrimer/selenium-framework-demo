import json
import os
import pytest
from selenium.webdriver import Chrome, Firefox, ChromeOptions
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utilities.custom_logger import custom_logger


logger = custom_logger()
BASE_URL = "https://www.topman.com/"


@pytest.fixture(scope='session')
def config():
    root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(root, "src", "config.json")
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="session")
def driver_setup(config):
    browser = config['BROWSER']
    options = ChromeOptions()
    if browser == "chrome":
        driver = Chrome(options=options)
        logger.info("Opened Chrome window")
    elif browser == "firefox":
        driver = Firefox()
        logger.info("Opened Firefox window")
    else:
        raise Exception(f"Unsupported browser, can't open {browser}")
        
    driver.maximize_window()
    driver.get(BASE_URL)
    logger.info(f"Go to URL:: {BASE_URL}")
    driver.implicitly_wait(config['WAIT_TIME'])
    yield driver
    login_page = LoginPage(driver)
    cart = CartPage(driver)
    if login_page.verify_logged_in():
        cart.goto()
        if not cart.verify_empty_cart():
            cart.clear_cart()
        login_page.sign_out()
    driver.close()
