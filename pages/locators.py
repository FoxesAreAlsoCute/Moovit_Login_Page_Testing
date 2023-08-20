from selenium.webdriver.common.by import By

class LoginPageLocators():
    EMAIL_INPUT = (By.ID, "email_input")
    PASSWORD_INPUT = (By.ID, "password_input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-automation].button[type='submit']")
    FORGOT_PASSWORD_BUTTON = (By.CLASS_NAME, "forgot-pass")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

class ForgetPasswordPageLocators():
    RESET_BUTTON = (By.CSS_SELECTOR, '.button.button--primary[data-automation="login-button"]')