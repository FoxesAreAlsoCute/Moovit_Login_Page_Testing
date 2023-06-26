from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\n\nOpen chrome browser...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\n\nQuit browser...\n\n")
    browser.quit()