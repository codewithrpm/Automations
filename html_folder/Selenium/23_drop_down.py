from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

# Bootstrap drop down
driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

countryLists = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(f"Length of the country lists are : {len(countryLists)}")

for country in countryLists:
    if country.text == "India":
        country.click()
        break
# Taking screenshot
driver.get_screenshot_as_file("screenshot.png")

time.sleep(3)
driver.quit()