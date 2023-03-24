import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://netbanking.hdfcbank.com/netbanking/")

driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))

# enter userid as test123
driver.find_element(By.NAME, "fldLoginUserId").send_keys("test123")
driver.find_element(By.LINK_TEXT,"CONTINUE").click()

driver.switch_to.default_content()

time.sleep(5)
driver.quit()
