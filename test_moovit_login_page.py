from pages.login_page import LoginPage
from pages.forget_password_page import ForgetPasswordPage
from selenium.webdriver.common.by import By
import pytest

link = "https://accounts.b2b.qa.moovit.com/login"

@pytest.mark.smoke
def test_user_can_access_to_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_user_cannot_login_with_empty_field(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.the_login_button_should_be_disabled()

@pytest.mark.xfail(reason="Need to get the correct login and password")
def test_user_can_login_to_website(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.log_in("qwerty@example.com", "qwerty")

def test_user_can_access_to_forget_password_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.go_to_forget_password_page()
    page = ForgetPasswordPage(browser, browser.current_url)
    page.should_be_forget_password_page()
