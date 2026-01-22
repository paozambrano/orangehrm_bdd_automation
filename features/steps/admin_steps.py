from behave import given, when, then
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@given('I navigate to the OrangeHRM login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to("https://opensource-demo.orangehrmlive.com/")

@when ('I login with username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.login_page.login_to_orange(user, pwd)

@then('I should be on the Dashboard page')
def step_impl(context):
    assert "dashboard" in context.driver.current_url.lower()

@given('I navigate to the Admin User Management page')
def step_impl(context):
    context.admin_page = AdminPage(context.driver)
    context.admin_page.go_to_admin_tab()

@when('I click on the Add button')
def step_impl(context):
    context.admin_page.click_add()

@when('I fill the user form with "{role}", "{employee_name}", "{username}" and "{password}"')
def step_impl(context, role, employee_name, username, password):
    context.admin_page.fill_user_details(role, employee_name, username, password)

@when('I click on Save')
def step_impl(context):
    context.admin_page.save_user()

@then('I should be able to find "{username}" in the user table')
def step_impl(context, username):
    time.sleep(3)
    user_locator = (By.XPATH, f"//div[text()='{username}']")

    result = context.admin_page.wait.until(EC.presence_of_element_located(user_locator))
    assert result is not None, f"No se encontró el usuario {username} en la tabla"