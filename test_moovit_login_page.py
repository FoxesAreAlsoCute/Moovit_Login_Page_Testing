from selenium.webdriver.common.by import By
import pytest

link = "https://accounts.b2b.qa.moovit.com/login"

# assert the modules
def assert_the_modules(browser):
    # open the link
    browser.get(link)
    # the email field
    email_field = browser.find_elements(By.ID, "email_input")
    assert email_field.__len__() > 0, "There is no email field!"
    # the password field
    password_field = browser.find_elements(By.ID, "password_input")
    assert password_field.__len__() > 0, "There is no password field!"
    # the login button
    login_button = browser.find_elements(By.CSS_SELECTOR, "[data-automation].button[type='submit']")
    assert login_button.__len__() > 0, "There is no login button!"
    # the forgot password button
    forgot_password_button = browser.find_elements(By.CLASS_NAME, "forgot-pass")
    assert forgot_password_button.__len__() > 0, "There is no forgot-password button"


@pytest.mark.smoke
def smoke_test(browser):
    print("\nsmoke test starts...")
    assert_the_modules(browser)


def test_null_input(browser):
    print("\nnull input test starts...")
    assert_the_modules(browser)
    assert browser.find_element(By.CSS_SELECTOR, "[data-automation].button[type='submit']").get_attribute("disabled"), "The login button is enabled!"


@pytest.mark.xfail(reason="Need to get the correct login and password and then to write the assert")
def test_valid_login(browser):
    print("\nvalid login test starts...")
    assert_the_modules(browser)
    # try to login
    browser.find_element(By.ID, "email_input").send_keys("")
    browser.find_element(By.ID, "password_input").send_keys("")
    browser.find_element(By.CSS_SELECTOR, "[data-automation].button[type='submit']").click()
    # then we have to type something here...


def test_invalid_login(browser):
    print("\ninvalid login test starts...")
    assert_the_modules(browser)
    # try to login
    browser.find_element(By.ID, "email_input").send_keys("lorem ipsum")
    browser.find_element(By.ID, "password_input").send_keys("lorem ipsum")
    browser.find_element(By.CSS_SELECTOR, "[data-automation].button[type='submit']").click()
    error_message = browser.find_elements(By.CSS_SELECTOR, "div.error-message").__len__()
    assert error_message > 0, "There is no error message!"


def test_forgot_password_button_work(browser):
    print("\nforgot password test starts...")
    assert_the_modules(browser)
    browser.find_element(By.CLASS_NAME, "forgot-pass").click()
    # just try to  find the reset button
    reset_password_button = browser.find_elements(
        By.CSS_SELECTOR, '.button.button--primary[data-automation="login-button"]'
        )
    assert reset_password_button.__len__() > 0, "There is no reset button!"
