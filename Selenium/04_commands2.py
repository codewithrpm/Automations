from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.in/")
driver.get("https://www.facebook.com/")
# wait commands
driver.implicitly_wait(10)

# Navigational commands:
driver.back() # amazon
# Wait commands
# time.sleep(3)
driver.forward() # facebook
driver.refresh()
driver.quit()