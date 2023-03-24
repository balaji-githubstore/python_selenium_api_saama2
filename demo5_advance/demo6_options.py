import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_argument("start-maximized")
opt.add_argument("--disable-notifications")
opt.add_argument("--headless")


driver = webdriver.Chrome(options=opt)
# driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.irctc.co.in/nget/train-search")

print(driver.title)


time.sleep(5)
driver.quit()



