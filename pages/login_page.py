from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "No login in url address"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form can't find"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form can't find"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        input_email.send_keys(email)
        input_psw = self.browser.find_element(*LoginPageLocators.REG_PSW)
        input_psw.send_keys(password)
        input_psw_c = self.browser.find_element(*LoginPageLocators.REG_PSW2)
        input_psw_c.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()
