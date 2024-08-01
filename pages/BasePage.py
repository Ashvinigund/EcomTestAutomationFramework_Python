from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This page is parent class to all pages and contains generic methods and utility for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def type_into_element(self, text, locator):
        # Get the element
        element = self.get_element(locator)

        # Scroll the element into view (optional but often useful)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Clear any existing text
        element.clear()

        # Type the text into the element
        element.send_keys(text)

    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator, timeout=20):
        """Check if element is visible on the page."""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            print(f"Element with locator {by_locator} not found within {timeout} seconds.")
            return False

    def check_display_status_of_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()
