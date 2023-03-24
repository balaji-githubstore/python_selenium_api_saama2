# Task 1 (Please check after 5 PM IST. Site may not work between 2 to 5 PM IST)
# 1.	Navigate onto http://demo.openemr.io/b/openemr/
# 2.	Update username as admin
# 3.	Update password as pass
# 4.	Select language as English (Indian)
# 5.	Click on the login button
# 6.	Click on Patient  Click New Search
# 7.	Add the first name, last name
# 8.	Update DOB as today's date
# 9.	Update the gender
# 10.	. Click on the create new patient button above the form
# 11.	. Click on confirm create new patient button.
# 12.	. Print the text from alert box (if any error before handling alert add 5 sec wait)
# 13.	. Handle alert
# 14.	Close the Happy Birthday popup
# 15.	Get the added patient name and print in the console.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.openemr.io/b/openemr")

driver.find_element(By.ID,"authUser").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"#clearPass").send_keys("pass")

select_lan=Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_lan.select_by_visible_text("English (Indian)")

driver.find_element(By.CSS_SELECTOR,"#login-button").click()

driver.find_element(By.XPATH,"//div[text()='Patient']").click()
driver.find_element(By.XPATH,"//div[text()='New/Search']").click()

#check for frame before entering firstname

driver.find_element(By.ID,"form_fname").send_keys("kevin")

time.sleep(5)
driver.quit()
