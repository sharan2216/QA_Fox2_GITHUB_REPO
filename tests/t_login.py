from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-email").send_keys("sksharan666@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "input-password").send_keys("155113412")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        actual_text = self.driver.find_element(By.XPATH, "//a[text()='Edit your account information']").text
        expected_text = "Edit your account information"
        assert actual_text.__eq__(expected_text)

    def test_login_with_invalid_email_and_valid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-email").send_keys("sksharan666000@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "input-password").send_keys("155113412")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        # actual_text=driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
        # expected_text="Edit your account information"
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        # expected_warning_message = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        actual_warning_message = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
        assert expected_warning_message.__contains__(actual_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-email").send_keys("sksharan666@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "input-password").send_keys("155113412000")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        # actual_text = driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
        expected_text = "Edit your account information"
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        # expected_warning_message = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        actual_warning_message = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
        assert expected_warning_message.__contains__(actual_warning_message)

    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
        time.sleep(2)
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        # actual_text=driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
        # expected_text="Edit your account information"
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        # expected_warning_message = "Warning: Your accoud allowed nunt has exceedember of login attempts. Please try again in 1 hour."
        actual_warning_message = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
        assert expected_warning_message.__contains__(actual_warning_message)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "sksharan666" + time_stamp + "@gmail.com"

