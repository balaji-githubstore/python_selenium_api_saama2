#mouse actions
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://nasscom.in/")


action=webdriver.ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Membership']")).perform()

driver.find_element(By.XPATH,"//a[text()='Members Listing']").click()



time.sleep(5)
driver.quit()

