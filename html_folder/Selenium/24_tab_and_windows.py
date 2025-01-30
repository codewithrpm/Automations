from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# Find the "Register" link
register_link = driver.find_element(By.LINK_TEXT, "Register")

# Open the link in a new tab using ActionChains
ActionChains(driver).key_down(Keys.CONTROL).click(register_link).key_up(Keys.CONTROL).perform()

# Wait for observation (optional)
time.sleep(2)

# Quit the driver
driver.quit()
