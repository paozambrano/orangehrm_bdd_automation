from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def login_to_orange(self, user, pwd):
        self.type_text(self.USERNAME_INPUT, user)
        self.type_text(self.PASSWORD_INPUT, pwd)
        self.click_element(self.LOGIN_BUTTON)