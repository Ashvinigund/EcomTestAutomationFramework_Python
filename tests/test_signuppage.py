import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.BaseTest import BaseTest  # Assuming handle_alert is in BaseTest


@pytest.mark.usefixtures("init_driver")
class TestSignUpPage(BaseTest):  # Inherit from BaseTest

    def test_verify_is_user_exists(self):
        """Test to verify the behavior when a user already exists."""
        # Wait for and click the sign-up link
        signup_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "signin2"))
        )
        signup_link.click()

        # Wait for the sign-up username field and send keys
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sign-username"))
        )
        username_field.send_keys("Test_Cuser")

        # Wait for the sign-up password field and send keys
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sign-password"))
        )
        password_field.send_keys("user1234")

        # Wait for the sign-up button to be clickable and click it
        signup_submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign up']"))
        )
        signup_submit_button.click()

        # Handle the alert that appears after attempting to sign up
        self.handle_alert(self.driver, expected_text="This user already exist.")

    def test_signup_new_user(self):
        """Test to sign up a new user and verify successful sign-up."""
        # Wait for and click the sign-up link
        signup_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signin2"))
        )
        signup_link.click()

        # Wait for the sign-up username field and send keys
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sign-username"))
        )
        username_field.send_keys("Test_Cuser9")

        # Wait for the sign-up password field and send keys
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sign-password"))
        )
        password_field.send_keys("user123456")

        # Wait for the sign-up button to be clickable and click it
        signup_submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign up']"))
        )
        signup_submit_button.click()

        # Handle the alert that appears after attempting to sign up
        self.handle_alert(self.driver, expected_text="Sign up successful.")
