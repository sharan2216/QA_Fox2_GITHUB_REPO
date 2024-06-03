from select import select
from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
driver.implicitly_wait(10)
month=driver.find_element(By.XPATH,"//select[@id='month']")
monthdd=Select(month)
monthdd.select_by_index(3)
time.sleep(3)
monthdd.select_by_value("6")
time.sleep(3)
monthdd.select_by_visible_text("Aug")
time.sleep(3)

ddlist=monthdd.options
for ele in ddlist:
    print("Value is :",ele.text)
    if ele.text=='Nov':
        ele.click()
        break
driver.implicitly_wait(10)