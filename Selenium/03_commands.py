from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Application commands:
driver.get("https://www.amazon.in/")
driver.implicitly_wait(20)
print(driver.title)
print(driver.current_url)
# print(driver.page_source)

# Conditional commands:
searchBox = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
searchBox.send_keys("Oneplus")
print(f"Display Status : {searchBox.is_displayed()}")
print(f"Enable Status : {searchBox.is_enabled()}")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
oneplus = driver.find_element(By.XPATH, "//span[text()='OnePlus']")
print(f"Selected status : {oneplus.is_selected()}")

# Browser command
driver.quit()