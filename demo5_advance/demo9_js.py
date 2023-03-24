import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""extracting data from graph, video using js"""
driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.youtube.com/watch?v=5FUdrBq-WFo")
time.sleep(5)
res=driver.execute_script("return document.querySelectorAll('[class=\"video-stream html5-main-video\"]')[0].duration")
print(res)
res=driver.execute_script("return document.querySelectorAll('[class=\"video-stream html5-main-video\"]')[0].currentTime")
print(res)
res=driver.execute_script("return document.querySelectorAll('[class=\"video-stream html5-main-video\"]')[0].videoWidth")
print(res)
res=driver.execute_script("return document.querySelectorAll('[class=\"video-stream html5-main-video\"]')[0].volume")
print(res)
time.sleep(5)
driver.quit()
