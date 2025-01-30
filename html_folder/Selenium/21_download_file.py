from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set Chrome options to customize download behavior
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "C:\\Users\\rupam\\Downloads",  # Specify your download directory
    "download.prompt_for_download": False,  # Disable the download prompt
    "directory_upgrade": True,  # Ensure directory exists
    "safebrowsing.enabled": True  # Enable safe browsing to avoid blocking
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(),options=chrome_options))
driver.get("https://file-examples.com/index.php/sample-audio-files/")
driver.maximize_window()
driver.implicitly_wait(10)

# Scroll the element into view to ensure it's visible
download = driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/a[1]")
# download.click()
driver.execute_script("arguments[0].scrollIntoView();", download)
time.sleep(2)  # Give some time for scrolling to complete

# Use JavaScript to click the element
driver.execute_script("arguments[0].click();", download)

time.sleep(10)
driver.quit()
