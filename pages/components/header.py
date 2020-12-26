from selenium.webdriver.common.by import By

# locators
SEARCH_BAR = (By.ID, 'searchTermInput')
SEARCH_BTN = (By.XPATH, "//button[@class='SearchBar-button'][1]")
HOME_LINK = (By.XPATH, "//a[@class='HeaderTopman-brandLink']")
ACCOUNT_BTN = (By.XPATH, "//span[contains(@class, 'AccountIcon-icon')]")
SIGN_OUT_LINK = (By.XPATH, "//a[@class='AccountIcon-popoverButton AccountIcon-popoverButtonSignOut']")
WISHLIST_LINK = (By.XPATH, "//div[@class='HeaderTopman-wishlist']//a[@class='WishlistHeaderLink']")
CART_LINK = (By.XPATH, "//button[contains(@class, 'ShoppingCart')]")