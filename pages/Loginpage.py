from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    """Page object for the login page, containing methods for interacting with login elements."""

    # Page locators (Object Repository)
    Loginlink = (By.ID, "login2")
    Username = (By.ID, "loginusername")
    Password = (By.ID, "loginpassword")
    Loginbtn = (By.XPATH, "//button[text()='Log in']")
    Logoutbtn = (By.ID, "logout2")

    def __init__(self, driver):
        """Initialize the page with the WebDriver instance."""
        super().__init__(driver)

    def is_loginlink_visible(self):
        """Check if the login link is visible."""
        return self.is_visible(self.Loginlink)

    def enter_username(self, username_text):
        """Enter the username into the username field."""
        self.type_into_element(username_text, self.Username)

    def enter_password(self, password_text):
        """Enter the password into the password field."""
        self.type_into_element(password_text, self.Password)

    def click_on_login_button(self):
        """Click on the login button."""
        self.do_click(self.Loginbtn)

    def login_to_application(self, username_text, password_text):
        """Log into the application using provided username and password."""
        self.enter_username(username_text)
        self.enter_password(password_text)
        self.click_on_login_button()

    def is_logoutbtn_visible(self):
        """Check if the logout button is visible after login."""
        return self.is_visible(self.Logoutbtn)
