import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("start-maximized")

dic = {"download.default_directory": "C:\\mine"}
opt.add_experimental_option("prefs", dic)

# opt.add_experimental_option("mobileEmulation",{"deviceName":"Pixel 5"})

driver = webdriver.Chrome(options=opt)
# driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://selenium.dev/downloads")

print(driver.title)
driver.find_element(By.PARTIAL_LINK_TEXT, "32").click()

driver.switch_to.new_window("tab")
driver.get("chrome://downloads/")

# get the text - show in folder
# actual_value=driver.find_element(By.ID,"show").text

# document.querySelector("body > downloads-manager")\
#     .shadowRoot.querySelector("#frb0")\
#     .shadowRoot.querySelector("#show")

sr=driver.find_element(By.XPATH,"//downloads-manager").shadow_root
sr=sr.find_element(By.CSS_SELECTOR,"#frb0").shadow_root
actual_value=sr.find_element(By.CSS_SELECTOR,"#show").text

print(actual_value)
time.sleep(20)
driver.quit()
