from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutProcess:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.cart_btn_locator = (By.ID, "cartur")
        self.place_order_btn_locator = (By.XPATH, "//button[normalize-space()='Place Order']")
        self.name_field_locator = (By.ID, "name")
        self.country_field_locator = (By.ID, "country")
        self.city_field_locator = (By.ID, "city")
        self.card_field_locator = (By.ID, "card")
        self.month_field_locator = (By.ID, "month")
        self.year_field_locator = (By.ID, "year")
        self.purchase_btn_locator = (By.XPATH, "//button[normalize-space()='Purchase']")
        self.success_message_locator = (By.XPATH, "//h2[normalize-space()='Thank you for your purchase!']")

    def do_click(self, locator):
        """Click on an element identified by the given locator."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def click_on_cart_button(self):
        self.do_click(self.cart_btn_locator)

    # Fill out the checkout form
    def fill_checkout_form(self, name, country, city, credit_card, month, year):
        self.wait.until(EC.visibility_of_element_located(self.name_field_locator)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.country_field_locator)).send_keys(country)
        self.wait.until(EC.visibility_of_element_located(self.city_field_locator)).send_keys(city)
        self.wait.until(EC.visibility_of_element_located(self.card_field_locator)).send_keys(credit_card)
        self.wait.until(EC.visibility_of_element_located(self.month_field_locator)).send_keys(month)
        self.wait.until(EC.visibility_of_element_located(self.year_field_locator)).send_keys(year)

    # Click the Place Order button
    def click_place_order(self):
        place_order_btn = self.wait.until(EC.element_to_be_clickable(self.place_order_btn_locator))
        place_order_btn.click()

    # Click the Purchase button
    def click_purchase(self):
        purchase_btn = self.wait.until(EC.element_to_be_clickable(self.purchase_btn_locator))
        purchase_btn.click()

    # Verify if the order was successful
    def is_order_successful(self):
        try:
            success_message = self.wait.until(EC.visibility_of_element_located(self.success_message_locator))
            return success_message.is_displayed()
        except Exception:
            return False
