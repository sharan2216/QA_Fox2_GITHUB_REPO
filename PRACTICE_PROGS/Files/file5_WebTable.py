from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://qavbox.github.io/demo/webtable/")
driver.maximize_window()
time.sleep(3)
table=driver.find_element(By.ID,"table01")
body=driver.find_element(By.XPATH,"//table[@id='table01']/tbody")
rows=driver.find_elements(By.XPATH,"//table[@id='table01']/tbody/tr")
cell=driver.find_elements(By.XPATH,"//table[@id='table01']/tbody/tr/td")

print("len of rows :",len(rows))


for i in range(len(rows)):
    columns=driver.find_elements(By.XPATH,"//table[@id='table01']/tbody/tr/td")
    print(print("len of columns is:",len(columns)))
    for j in range(len(columns)):
        if i<=len(rows):
            print(cell[j].text)

