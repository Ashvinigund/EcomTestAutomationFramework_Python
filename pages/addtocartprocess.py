from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.mobile_locator = (By.XPATH, "//a[normalize-space()='Samsung galaxy s6']")
        self.laptop_locator = (By.XPATH, "//a[normalize-space()='Sony vaio i5']")
        self.add_to_cart_btn_locator = (By.XPATH, "//a[normalize-space()='Add to cart']")
        self.next_button_locator = (By.ID, "next2")
        self.last_product_locator = (By.XPATH, "//a[normalize-space()='MacBook Pro']")

    def do_click(self, locator):
        """Click on an element identified by the given locator."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def navigate_to_last_page(self):
        while True:
            try:
                next_button = self.wait.until(EC.element_to_be_clickable(self.next_button_locator))
                next_button.click()
            except Exception:
                break  # No more "Next" button to click or it is not clickable

    def add_to_cart(self):
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable(self.add_to_cart_btn_locator))
        add_to_cart_btn.click()
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
        except Exception as e:
            print(f"No alert present or unable to handle alert: {e}")

    def do_click_last_product(self, product_name):
        self.do_click(self.last_product_locator)
