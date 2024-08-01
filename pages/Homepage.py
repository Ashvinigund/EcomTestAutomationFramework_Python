from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from pages.Loginpage import LoginPage  # Ensure correct import path

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    Homepagelink = (By.XPATH, "//a[text()='Home']")
    Cat_Phones = (By.XPATH, "//a[text()='Phones']")
    Cat_Laptops = (By.XPATH, "//a[text()='Laptops']")
    Cat_Monitors = (By.XPATH, "//a[text()='Monitors']")
    LoginButton = (By.ID, "login2")  # Assuming this is the correct locator for the login button

    def do_click_phones(self):
        self.do_click(self.Cat_Phones)

    def do_click_laptops(self):
        self.do_click(self.Cat_Laptops)

    def do_click_monitors(self):
        self.do_click(self.Cat_Monitors)

    def navigate_to_homepage(self):
        self.do_click(self.Homepagelink)

    def navigate_to_login_page(self):
        # Ensure the login button is visible and clickable
        self.wait.until(EC.element_to_be_clickable(self.LoginButton))
        self.do_click(self.LoginButton)
        return LoginPage(self.driver)

    def is_login_page(self):
        # Check for the presence of an element unique to the login page
        # For example, if there's an input field with id 'login-username' on the login page
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
            return True
        except:
            return False
