import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time
from utilities import ReadConfigurations
from utilities import ReadConfigurations

@pytest.fixture()
def setup_and_teardown(request):
    # browser = ReadConfigurations.read_configurations("basic info","browser")
    browser="chrome"
    # # driver=None
    # # driver=webdriver.Chrome()
    # if browser.__eq__("chrome"):
    #     driver=webdriver.Chrome()
    # else:
    #     print("enter valid browser")
    driver=webdriver.Chrome()
    driver.maximize_window()
    app_url = "https://tutorialsninja.com/demo/"
    #app_url=ReadConfigurations.read_configurations("basic info","url")
    driver.get(app_url)
    # driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()