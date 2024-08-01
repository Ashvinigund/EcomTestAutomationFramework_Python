import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    @staticmethod
    def handle_alert(driver: WebDriver, expected_text: str = None) -> str:

        try:
            # Wait for the alert to be present
            WebDriverWait(driver, 10).until(EC.alert_is_present())

            # Switch to the alert
            alert = driver.switch_to.alert

            # Get alert text
            alert_text = alert.text
            # Log alert text (if logging is configured)
            print(f"Alert text: {alert_text}")

            # Accept the alert
            alert.accept()

            # Check if the expected text is in the alert
            if expected_text and expected_text not in alert_text:
                raise AssertionError(f"Expected text '{expected_text}' not found in alert. Actual: '{alert_text}'")

            return alert_text
        except Exception as e:
            print(f"Error handling alert: {str(e)}")  # Print for debugging
            raise AssertionError(f"Error handling alert: {str(e)}")
