import pytest
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.Homepage import HomePage
from tests.BaseTest import BaseTest


class TestHomepage(BaseTest):

    def test_products_displayed(self):
        home_page = HomePage(self.driver)
        base_page = BasePage(self.driver)

        # Dictionary to map product names to their locators
        product_locators = {
            "Samsung galaxy s6": (By.XPATH, "//a[text()='Samsung galaxy s6']"),
            "Sony vaio i5": (By.XPATH, "//a[text()='Sony vaio i5']"),
            "MacBook Pro": (By.XPATH, "//a[text()='MacBook Pro']")
        }

        # Iterate over each product and check if it is visible
        for product_name, locator in product_locators.items():
            try:
                is_visible = base_page.is_visible(locator)
                # Log the result
                print(f"Checking if '{product_name}' is visible: {is_visible}")
                # Assert that the product is visible
                assert is_visible, f"Product '{product_name}' is not displayed on the homepage."
            except Exception as e:
                # Log the exception and fail the test
                print(f"Error while checking visibility for '{product_name}': {str(e)}")
                assert False, f"Exception occurred: {str(e)}"

    def test_category_navigation(self):
        home_page = HomePage(self.driver)

        # Navigate to Phones category and verify
        home_page.do_click_phones()
        assert "Phones" in self.driver.title, f"Failed to navigate to Phones category. Current title: '{self.driver.title}'"

        # Navigate back to homepage
        home_page.navigate_to_homepage()

        # Navigate to Laptops category and verify
        home_page.do_click_laptops()
        assert "Laptops" in self.driver.title, f"Failed to navigate to Laptops category. Current title: '{self.driver.title}'"

        # Navigate back to homepage
        home_page.navigate_to_homepage()

        # Navigate to Monitors category and verify
        home_page.do_click_monitors()
        assert "Monitors" in self.driver.title, f"Failed to navigate to Monitors category. Current title: '{self.driver.title}'"
