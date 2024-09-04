from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.username_field = (By.NAME, "username")  # Ensure these locators are correct
        self.password_field = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        try:
            print("Entering username")
            username_element = self.wait.until(EC.visibility_of_element_located(self.username_field))
            username_element.send_keys(username)

            print("Entering password")
            password_element = self.wait.until(EC.visibility_of_element_located(self.password_field))
            password_element.send_keys(password)

            print("Clicking login button")
            login_button_element = self.wait.until(EC.element_to_be_clickable(self.login_button))
            login_button_element.click()

            print("Login action performed")
        except Exception as e:
            print(f"Error during login: {e}")
            raise

    def is_login_successful(self):
        try:
            # Check if login is successful by URL or element presence
            return self.wait.until(EC.url_contains("dashboard"))  # Adjust as needed
        except Exception as e:
            print(f"Login failed: {e}")
            return False
