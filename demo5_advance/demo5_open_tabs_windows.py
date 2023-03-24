import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://google.com/")

print(driver.title)

driver.switch_to.new_window('window')

driver.get("http://gmail.com")
gmail_title=driver.title

#switch to first tab
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.NAME,"q").send_keys(gmail_title)


time.sleep(5)
driver.quit()