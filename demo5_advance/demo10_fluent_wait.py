import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, InvalidSelectorException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://google.com")


wait = WebDriverWait(driver, 20,poll_frequency=0.5,ignored_exceptions=(Exception))
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@name='q"))).send_keys('hello')
wait.until(expected_conditions.alert_is_present())
time.sleep(5)
driver.quit()