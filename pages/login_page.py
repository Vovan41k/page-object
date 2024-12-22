from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        mail.send_keys(email)
        
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1.send_keys(password)

        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2.send_keys(password)
        
        button_submit = self.browser.find_element(*LoginPageLocators.REGISET_BUTTON_SUBMIT)
        button_submit.click()
        
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Invalid url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'