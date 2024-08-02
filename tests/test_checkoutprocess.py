from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.Homepage import HomePage
from pages.checkoutprocess import CheckoutProcess
from tests.BaseTest import BaseTest


class Testcheckoutprocess(BaseTest):

    def test_successful_checkout_with_items(self):
        home_page = HomePage(self.driver)
        checkoutprocess = CheckoutProcess(self.driver)
        checkoutprocess.click_on_cart_button()
        checkoutprocess.click_place_order()

        # Fill out the checkout form
        checkoutprocess.fill_checkout_form(
            name="John Doe",
            country="USA",
            city="New York",
            credit_card="4111111111111111",
            month="12",
            year="2024"
        )

        # Click Purchase
        checkoutprocess.click_purchase()

        # Verify if the order was successful
        assert checkoutprocess.is_order_successful()

    def test_checkout_with_empty_cart(self):
        home_page = HomePage(self.driver)
        checkout_process = CheckoutProcess(self.driver)

        # Navigate to cart and ensure it is empty
        home_page.do_click_cart()


        # Click Place Order
        checkout_process.click_place_order()

        # Verify if there is an error message or handling for empty cart
        try:
            # You might need to wait for the message to appear
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[text()='Your cart is empty']"))
            )
            assert True, "Error message for empty cart is displayed."
        except Exception:
            assert False, "No error message displayed for empty cart or unexpected behavior."
