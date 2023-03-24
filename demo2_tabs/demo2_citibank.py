"""
Task 3 – Important
1.	Navigate onto https://www.online.citibank.co.in/
2.	Close if any pop up comes
3.	Click on Login
4.	Click on Forgot User ID?
5.	Choose Credit Card
6.	Enter credit card number as 4545 5656 8887 9998
7.	Enter cvv number
8.	Enter date as “14/04/2022”
9.	Click on Proceed
10.	 Get the text and print it “Please accept Terms and Conditions”
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.online.citibank.co.in/")

driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()

# switch to second tab
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, "//div[contains(text(),'Forgot User')]").click()

driver.find_element(By.LINK_TEXT, "select your product type").click()
driver.find_element(By.LINK_TEXT, "Credit Card").click()

driver.find_element(By.ID, "citiCard1").send_keys("7887")
driver.find_element(By.ID, "citiCard2").send_keys("7887")
driver.find_element(By.ID, "citiCard3").send_keys("7887")
driver.find_element(By.ID, "citiCard4").send_keys("7887")

driver.find_element(By.CSS_SELECTOR, "#cvvnumber").send_keys("887")

# approach 1 #not working
# driver.find_element(By.ID, "bill-date-long").send_keys("14/04/2010")

# approach 2  #working
# driver.find_element(By.ID, "bill-date-long").click()
#
# select_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
# select_year.select_by_visible_text("2000")
#
# select_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
# select_month.select_by_visible_text("Apr")
#
# driver.find_element(By.LINK_TEXT, "14").click()

# approach 3
driver.execute_script("document.querySelector('#bill-date-long').value='14/04/2010'")

# Alertnate way of using javascript
# selenium build the javascript for us

element = driver.find_element(By.XPATH, "//input[@id='bill-date-long']")
driver.execute_script("arguments[0].value='14/04/1999'",element)

# 9.	Click on Proceed
driver.find_element(By.XPATH,"//input[@value='PROCEED']").click()

# 10.	 Get the text and print it “Please accept Terms and Conditions”

actual_error=driver.find_element(By.XPATH,"//li[contains(text(),'Terms and Con')]").text
print(actual_error)


actual_error=driver.find_element(By.XPATH,"//div[@role='dialog']").text
print(actual_error)


time.sleep(5)
driver.quit()

