from .base_page import BasePage
from .locators import ForgetPasswordPageLocators

class ForgetPasswordPage(BasePage):
    def should_be_forget_password_page(self):
        self.should_be_reset_button()

    def should_be_reset_button(self):
        assert self.is_element_present(*ForgetPasswordPageLocators.RESET_BUTTON), "Reset button is not present!"
