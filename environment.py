from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

def before_scenario(context, scenario):
    print(f"Starting Scenario: {scenario.name}")
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

    def after_scenario(context, scenario):
        if context.driver:
            print(f"Finishing scenario: {scenario.name}")
            context.driver.quit()