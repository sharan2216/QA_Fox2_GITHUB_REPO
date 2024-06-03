
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_valid_products(self):
        time.sleep(2)
        expected_title = "Your Store"
        actual_title = self.driver.title
        if actual_title.__eq__(expected_title):
            print("Title Matched")
        time.sleep(2)
        assert expected_title.__eq__(actual_title)
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default btn-lg')]").click()
        time.sleep(2)
        print("NEXT ASSERTION line printed here")
        ele = self.driver.find_element(By.LINK_TEXT, "HP LP3065")
        assert ele.is_displayed()

    def test_search_for_an_invalid_product(self):
        time.sleep(2)
        self.driver.find_element(By.NAME, "search").send_keys("HONDA")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default btn-lg')]").click()
        time.sleep(2)
        print("NEXT ASSERTION line printed here")
        ele_text = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        expected_text = "There is no product that matches the search criteria."
        assert ele_text.__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        time.sleep(2)
        self.driver.find_element(By.NAME, "search").send_keys("")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default btn-lg')]").click()
        time.sleep(2)
        print("NEXT ASSERTION line printed here")
        ele_text = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        expected_text = "There is no product that matches the search criteria."
        assert ele_text.__eq__(expected_text)



