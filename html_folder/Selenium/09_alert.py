from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("Welcome Rupam")
alert_window.accept() # accept the alert by pressing ok
# alert_window.dismiss() # cancel the alert
time.sleep(3)
driver.quit()


