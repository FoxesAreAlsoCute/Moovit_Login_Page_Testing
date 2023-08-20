from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except(TimeoutException):
            return True
        return False
    
    def is_dissapeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except(TimeoutException):
            return False
        return True

    def is_disabled(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_attribute_to_include((how, what), "disabled"))
        except(TimeoutException):
            return False
        return True
    
    def is_enabled(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_attribute_to_include((how, what), "enabled"))
        except(TimeoutException):
            return False
        return True
    
    def element_is_clickable(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except(TimeoutException):
            return False
        return True
    
    def click_element(self, how, what):
        assert self.element_is_clickable(how, what), f"Element {what} is not clickable!"
        self.browser.find_element(how, what).click()
