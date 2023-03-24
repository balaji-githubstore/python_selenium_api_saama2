import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.facebook.com/")  # wait for the page load to complete

driver.find_element(By.LINK_TEXT, "Create new account").click()  # will check for presence of element in 0.5s

driver.find_element(By.NAME, "firstname").send_keys("bala")
driver.find_element(By.NAME, "lastname").send_keys("dina")

driver.find_element(By.ID,"password_step_input").send_keys("welcome123")

#dob - 25 Dec 2001

#select 25
select_day=Select(driver.find_element(By.ID,"day"))
select_day.select_by_visible_text("25")

select_month=Select(driver.find_element(By.ID,"month"))
select_month.select_by_visible_text("Dec")
# select_month.select_by_value("12")
# select_month.select_by_index(11)

select_year=Select(driver.find_element(By.XPATH,"//select[@title='Year']"))
select_year.select_by_visible_text("2001")

driver.find_element(By.XPATH,"//input[@value='-1']").click()

# driver.find_element(By.XPATH,"//label[text()='Custom']").click()

time.sleep(5)
driver.quit()
