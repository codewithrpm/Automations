from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(5)
driver.quit()

# When we have to handle authentication pop-up window, will have to enter the username and password.
# But we can't inspect the page so we have pass the username and password in the url itself, this method called as injection method.
# Syntax : https://username:password@url.com
# https://the-internet.herokuapp.com/basic_auth -> In this url authentication pop-up will come
# example : https://admin:admin@the-internet.herokuapp.com/basic_auth