from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page=HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page=LoginPage(self.driver)
        login_page.enter_email_address("sksharan666@gmail.com")
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)
        # self.driver.find_element(By.ID, "input-email").send_keys("sksharan666@gmail.com")
        time.sleep(2)
        login_page.enter_password("155113412")
        # self.driver.find_element(By.ID, "input-password").send_keys("155113412")
        login_page.click_on_login_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        account_page=AccountPage(self.driver)
        assert account_page.display_status_of_edit_your_account_information_option()
        # actual_text = self.driver.find_element(By.XPATH, "//a[text()='Edit your account information']").text
        # expected_text = "Edit your account information"
        # assert actual_text.__eq__(expected_text)

    def test_login_with_invalid_email_and_valid_password(self):
        home_page=HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address(self.generate_email_with_time_stamp)
        time.sleep(2)
        login_page.enter_password("155113412")
        time.sleep(2)
        login_page.click_on_login_button()
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # self.driver.find_element(By.LINK_TEXT, "Login").click()
        # time.sleep(2)
        # self.driver.find_element(By.ID, "input-email").send_keys("sksharan666000@gmail.com")
        # time.sleep(2)
        # self.driver.find_element(By.ID, "input-password").send_keys("155113412")
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        # actual_text=driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
        # expected_text="Edit your account information"
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        # expected_warning_message = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        actual_warning_message = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
        # assert expected_warning_message.__contains__(actual_warning_message)
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page=HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page=LoginPage(self.driver)
        login_page.enter_email_address("sksharan666@gmail.com")
        time.sleep(2)
        login_page.enter_password("100101010")
        time.sleep(2)
        login_page.click_on_login_button()


        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # self.driver.find_element(By.LINK_TEXT, "Login").click()
        # time.sleep(2)
        # self.driver.find_element(By.ID, "input-email").send_keys("sksharan666@gmail.com")
        # time.sleep(2)
        # self.driver.find_element(By.ID, "input-password").send_keys("155113412000")
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        # time.sleep(2)
        # actual_text = driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
        # expected_text = "Edit your account information"
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        # expected_warning_message = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        # actual_warning_message = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
        # assert expected_warning_message.__contains__(actual_warning_message)
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page=HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("")
        time.sleep(2)
        login_page.enter_password("")
        time.sleep(2)
        login_page.click_on_login_button()


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
        # actual_warning_message = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
        # assert expected_warning_message.__contains__(actual_warning_message)
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "sksharan666" + time_stamp + "@gmail.com"

