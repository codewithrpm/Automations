from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
# Send keys method to pass date
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("09/23/2026")

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

# Desired month, year, and date
Month = "October"  # Correct the format to the full month name
Year = "2025"
Date = "20"

while True:
    # Fetch the current month and year displayed in the date picker
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    # Check if the current month and year match the desired values
    if month == Month and year == Year:
        break
    else:
        # Click the "Next" button to go to the next month
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        time.sleep(1)  # Adding delay to wait for the next page to load

# Fetch all the dates in the calendar for the selected month
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

# Iterate over the dates and click on the desired date
for element in dates:
    if element.text == Date:
        element.click()
        break

driver.quit()
