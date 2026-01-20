from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class AdminPage(BasePage):
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    ADD_BUTTON = (By.XPATH, "//button[contains(.,'Add')]")

    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
    STATUS_DROPDOWN = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    USERNAME_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    PASSWORD_INPUT = (By.XPATH, "(//input[@type='password'])[1]")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "(//input[@type='password'])[2]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_admin_tab(self):
        self.click_element(self.ADMIN_MENU)

    def click_add(self):
        self.click_element(self.ADD_BUTTON)

    def fill_user_details(self, role, employee_name, username, password):

        self.click_element(self.USER_ROLE_DROPDOWN)
        self.click_element((By.XPATH, f"//span[text()='{role}']"))

        self.type_text(self.EMPLOYEE_NAME_INPUT, employee_name)
        time.sleep(2)
        self.click_element((By.XPATH, "//div[@role='option']"))

        self.click_element(self.STATUS_DROPDOWN)
        self.click_element((By.XPATH, "//span[text()='Enabled']"))

        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.type_text(self.CONFIRM_PASSWORD_INPUT, password)

    def save_user(self):
        self.click_element(self.SAVE_BUTTON)
