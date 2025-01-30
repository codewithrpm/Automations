from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.implicitly_wait(10)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
# Simulate pressing the Enter key / 'keys.RETURN' also work
search_box.send_keys(Keys.ENTER)
driver.quit()

