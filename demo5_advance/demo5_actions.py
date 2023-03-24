# mouse actions
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://google.com/")

action = webdriver.ActionChains(driver)

action.key_down(webdriver.Keys.SHIFT)\
    .send_keys("hello world")\
    .key_up(webdriver.Keys.SHIFT)\
    .pause(1)\
    .send_keys(webdriver.Keys.ARROW_DOWN)\
    .send_keys(webdriver.Keys.ARROW_DOWN)\
    .send_keys(webdriver.Keys.ARROW_DOWN) \
    .pause(1) \
    .send_keys(webdriver.Keys.ENTER)\
    .perform()

time.sleep(5)
driver.quit()
