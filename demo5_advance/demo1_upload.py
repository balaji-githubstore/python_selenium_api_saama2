import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://smallpdf.com/pdf-to-word")

driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Mine\Balaji-Profile_2023.pdf")


time.sleep(5)
driver.quit()
