
from datetime import datetime
import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


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
        home_page=HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        # self.driver.find_element(By.NAME, "search").send_keys("HP")
        time.sleep(2)
        home_page.click_on_search_button()
        # self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default btn-lg')]").click()
        time.sleep(2)
        print("NEXT ASSERTION line printed here")

        search_page = SearchPage(self.driver)
        search_page.display_status_of_valid_product()

        # ele = self.driver.find_element(By.LINK_TEXT, "HP LP3065")
        # assert ele.is_displayed()

    def test_search_for_an_invalid_product(self):
        home_page=HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HONDA")
        time.sleep(2)
        home_page.click_on_search_button()
        time.sleep(2)
        # self.driver.find_element(By.NAME, "search").send_keys("HONDA")
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default btn-lg')]").click()
        # time.sleep(2)
        print("NEXT ASSERTION line printed here")
        search_page = SearchPage(self.driver)
        # ele_text = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("")
        time.sleep(2)
        home_page.click_on_search_button()
        time.sleep(2)
        # self.driver.find_element(By.NAME, "search").send_keys("")
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default btn-lg')]").click()
        # time.sleep(2)
        print("NEXT ASSERTION line printed here")
        search_page = SearchPage(self.driver)
        # ele_text = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="retrieve_no_product_message",
                      attachment_type=AttachmentType.PNG)



