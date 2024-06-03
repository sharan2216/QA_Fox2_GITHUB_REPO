from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandate_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-firstname").send_keys("sk")
        self.driver.find_element(By.ID, "input-lastname").send_keys("sharan")
        # driver.find_element(By.ID,"input-email").send_keys(generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("9898989898")
        self.driver.find_element(By.ID, "input-password").send_keys("155113412")
        self.driver.find_element(By.ID, "input-confirm").send_keys("155113412")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        expected_heading_text = 'Your Account Has Been Created!'
        time.sleep(2)
        actual_heading_text = self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        assert expected_heading_text.__contains__(actual_heading_text)

    def test_Register_with_all_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-firstname").send_keys("sk")
        self.driver.find_element(By.ID, "input-lastname").send_keys("sharan")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("9898989898")
        self.driver.find_element(By.ID, "input-password").send_keys("155113412")
        self.driver.find_element(By.ID, "input-confirm").send_keys("155113412")
        self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value=1]").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        expected_heading_text = 'Your Account Has Been Created!'
        actual_heading_text = self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        assert expected_heading_text.__contains__(actual_heading_text)

    def test_Register_with_duplicate_email(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-firstname").send_keys("sk")
        self.driver.find_element(By.ID, "input-lastname").send_keys("sharan")
        self.driver.find_element(By.ID, "input-email").send_keys("sksharan666@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("9898989898")
        self.driver.find_element(By.ID, "input-password").send_keys("155113412")
        self.river.find_element(By.ID, "input-confirm").send_keys("155113412")
        self.river.find_element(By.NAME, "agree").click()
        self.self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        expected_warning_text = 'Warning: E-Mail Address is already registered!'
        actual_heading_text = self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text
        assert expected_warning_text.__contains__(actual_heading_text)

    def test_Register_without_any_input(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-firstname").send_keys()
        self.driver.find_element(By.ID, "input-lastname").send_keys()
        self.driver.find_element(By.ID, "input-email").send_keys()
        self.driver.find_element(By.ID, "input-telephone").send_keys()
        self.driver.find_element(By.ID, "input-password").send_keys()
        self.driver.find_element(By.ID, "input-confirm").send_keys()
        time.sleep(2)
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)

        expected_firstname_warning_message = 'First Name must be between 1 and 32 characters!'
        actual_firstname_warning_message = self.driver.find_element(By.XPATH,
                                                               "//input[@id='input-firstname']/following-sibling::div").text
        assert actual_firstname_warning_message.__contains__(expected_firstname_warning_message)

        expected_lastname_warning_message = 'First Name must be between 1 and 32 characters!'
        actual_lastname_warning_message = self.driver.find_element(By.XPATH,
                                                              "//input[@id='input-firstname']/following-sibling::div").text
        assert actual_lastname_warning_message.__contains__(expected_lastname_warning_message)

        expected_email_warning_message = 'E-Mail Address does not appear to be valid!'
        actual_email_warning_message = self.driver.find_element(By.XPATH,
                                                           "//input[@name='email']/following-sibling::div").text
        assert actual_email_warning_message.__contains__(expected_email_warning_message)

        expected_telephone_warning_message = 'Telephone must be between 3 and 32 characters!'
        actual_telephone_warning_message = self.driver.find_element(By.XPATH,
                                                               "//input[@id='input-telephone']/following-sibling::div").text
        assert actual_telephone_warning_message.__contains__(expected_telephone_warning_message)

        actual_password_warning_message = 'Password must be between 4 and 20 characters!'
        expected_password_warning_message = self.driver.find_element(By.XPATH,
                                                                "//input[@id='input-password']/following-sibling::div").text
        assert actual_password_warning_message.__contains__(expected_password_warning_message)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "sksharan6666" + time_stamp + "@gmail.com"
