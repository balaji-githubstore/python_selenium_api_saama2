import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.db4free.net/")

# click on phpMyAdmin »
driver.find_element(By.PARTIAL_LINK_TEXT, "phpMyAdmin").click()

# print(driver.window_handles)
# print(driver.window_handles[0])
# print(driver.window_handles[1])

# switch to second tab
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.ID,"input_username").send_keys("hello")
driver.find_element(By.ID,"input_password").send_keys("hello123")
driver.find_element(By.ID,"input_go").click()

driver.close()

# switch to first tab
driver.switch_to.window(driver.window_handles[0])
print(driver.title)

#added comment
#added comment 2
time.sleep(5)
driver.quit()
