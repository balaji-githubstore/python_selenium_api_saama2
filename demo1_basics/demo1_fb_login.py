import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver1=webdriver.Chrome()

driver.get("https://www.facebook.com/")

print(driver.title)
print(driver.current_url)
# print(driver.page_source)

driver1.get("https://www.google.com/")

print(driver.title)
print(driver.current_url)

ele1=driver.find_element(By.ID,'email')
ele1.send_keys("bala12345@gmail.com")

driver.find_element(By.ID,"email").send_keys("bala12345@gmail.com")
driver.find_element(By.ID,"pass").send_keys("welcome123")
#click on login
driver.find_element(By.NAME,"login").click()

time.sleep(5)

driver.quit()

