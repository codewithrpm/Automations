from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/India")
driver.maximize_window()
# Scroll by pixel
# driver.execute_script("window.scrollBy(0,3000)")
# time.sleep(3)

# Scroll by particular element
# img = driver.find_element(By.XPATH, "//figure[@class='noresize']//img[@class='mw-file-element']")
# driver.execute_script("arguments[0].scrollIntoView();",img)
# time.sleep(4)

# Scroll down till the page end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(4)
# # This is the way we can get page pixel value
# value = driver.execute_script("return window.pageYOffset;")
# print(value)

# Scroll up to the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(4)
driver.quit()
