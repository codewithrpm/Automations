from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

# Find all anchor tags
all_links = driver.find_elements(By.XPATH, "//a")
count = 0

for link in all_links:
    url = link.get_attribute("href")

    # Check if the URL is not empty or None
    if url is None or url == "":
        continue

    try:
        # Make a HEAD request to the URL
        response = requests.head(url)

        # Check if the status code indicates a broken link (400-499 or 500-599)
        if response.status_code >= 400:
            print(f"{url} is a broken link (status code: {response.status_code})")
            count += 1
        else:
            print(f"{url} is a valid link (status code: {response.status_code})")
    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")

print(f"Total number of broken links: {count}")
driver.quit()
