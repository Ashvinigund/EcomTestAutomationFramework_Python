
from pages.BasePage import BasePage
from pages.Homepage import HomePage
from pages.Loginpage import LoginPage
from tests.BaseTest import BaseTest


class TestLogout(BaseTest):

    def test_logout_successfully(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        base_page = BasePage(self.driver)
        login_page.login_to_application()
        # Ensure the logout button is visible
        assert login_page.is_logoutbtn_visible(), "Logout button is not visible on the login page."

        # Click the logout button
        base_page.do_click(login_page.logoutbtn_locator)

        # Verify that the user is redirected to the homepage or login page
        assert home_page.is_login_page()  # Assuming HomePage has a method to verify login page or relevant post-logout state
