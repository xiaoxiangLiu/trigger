from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# driver.maximize_window()
driver.implicitly_wait(30)
driver.get(url="https://www.baidu.com")

driver.find_element(By.ID, 'kw').send_keys("selenium")

time.sleep(2)
driver.find_element(By.ID, 'su').click()


time.sleep(2)
driver.close()

