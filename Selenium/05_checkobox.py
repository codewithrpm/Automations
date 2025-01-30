from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
driver.implicitly_wait(10)
# Select specific checkbox
# driver.find_element(By.XPATH,"//label[text()='Sports']").click()
# Select all checkboxes
checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='form-check-input mt-0']")
for checkbox in checkBoxes:
    checkbox.click()
time.sleep(5)