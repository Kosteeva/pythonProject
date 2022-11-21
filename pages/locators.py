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



