# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities import ReadConfigurations

@pytest.fixture(scope='class')
def init_driver(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Conditional navigation
    condition = True  # Replace with the actual condition logic
    if condition:
        driver.get("https://www.demoblaze.com/")
    else:
        app_url = ReadConfigurations.read_configuration("basic info", "url")
        driver.get(app_url)

    request.cls.driver = driver
    yield driver

    # Teardown: quit the driver to close all windows and end the session
    driver.quit()
