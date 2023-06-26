from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nOpen chrome browser...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nQuit browser...")
    browser.quit()