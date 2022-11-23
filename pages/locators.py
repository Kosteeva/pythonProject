from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PSW = (By.NAME, 'login-password')
    REG_FORM = (By.ID, 'register_form')
    REG_EMAIL = (By.NAME, 'registration-email')
    REG_PSW = (By.NAME, 'registration-password1')
    REG_PSW2 = (By.NAME, 'registration-password2')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, '.btn-group > .btn')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    ALERT_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    ALERT_BOOK_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, '.col-sm-4 a')
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, '.col-sm-1 p')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")





