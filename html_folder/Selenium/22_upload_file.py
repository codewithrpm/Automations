from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.monsterindia.com/seeker/registration")  # Example page with file upload
driver.maximize_window()
driver.implicitly_wait(10)

# Locate the file input element
file_input = driver.find_element(By.XPATH, "//input[@id='file-upload']")  # Adjust the XPath to your element

# Provide the full path to the file to upload
file_path = r"C:\Users\rupam\Downloads\example_file.pdf"  # Replace with your file path
file_input.send_keys(file_path)

# Wait to observe the file upload (optional)
time.sleep(5)

# Close the browser
driver.quit()
