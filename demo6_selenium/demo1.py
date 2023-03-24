import time

from selenium import webdriver

# from selenium.webdriver.chrome.webdriver import WebDriver
#
# d=WebDriver()
d=webdriver.Chrome()
d.get("https://www.google.com/")



time.sleep(5)
d.quit()
