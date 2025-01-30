from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field1.clear()
field1.send_keys("Hey Rupam.!")
time.sleep(3)
double_click = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
action = ActionChains(driver)
action.double_click(double_click).perform()
time.sleep(3)
driver.quit()