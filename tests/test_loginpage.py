import pytest
from tests.BaseTest import BaseTest
from pages.Homepage import HomePage
from utilities import ExcelUtils


class TestLogin(BaseTest):
    @pytest.mark.parametrize("username_text,password_text",
                             ExcelUtils.get_data_from_excel("ExcelFiles/LoginTestData.xlsx", "LoginTest"))
    def test_login_with_valid_credentials(self, username_text, password_text):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(username_text, password_text)
        assert login_page.is_logoutbtn_visible()

    def test_login_with_invalid_username_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("abc@gmail.com", "12345")
        expected_warning_message = "Warning: Wrong Username and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_username_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("test_user", "1234567890")
        expected_warning_message = "Warning: Wrong Username and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("", "")
        # Switch to the alert
        # Handle alert and check for expected message
        self.handle_alert(self.driver, expected_text="Wrong password")
