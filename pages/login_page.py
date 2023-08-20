from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_email_input()
        self.should_be_password_input()
        self.should_be_login_button()
        self.should_be_forgot_password_button()

    def should_be_email_input(self):
        print("should be email input..")
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT), "There is no email input!"

    def should_be_password_input(self):
        print("should be password input..")
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), "There is no password input!"

    def should_be_login_button(self):
        print("should be login button..")
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "There is no login button!"

    def should_be_forgot_password_button(self):
        print("should be forgot password button..")
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_BUTTON), "There is no forgot password button!"

    def the_login_button_should_be_disabled(self):
        print("the login button should be disabled..")
        assert self.is_disabled(*LoginPageLocators.LOGIN_BUTTON), "The login button is enabled!"

    def log_in(self, email, password):
        print("login..")
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
        assert self.is_not_element_present(*LoginPageLocators.ERROR_MESSAGE), "The error message is present!"

    def go_to_forget_password_page(self):
        print("go to forget password page..")
        self.click_element(*LoginPageLocators.FORGOT_PASSWORD_BUTTON)




        