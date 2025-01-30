from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# current_window = driver.current_window_handle
# print(current_window)

driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()

windowsID = driver.window_handles
# Parent_window = windowsID[0]
# Child_window = windowsID[1]
#
# print(f"Parent window {windowsID[0]}")
# print(f"Child window {windowsID[1]}")
#
# driver.switch_to.window(Child_window)
# print(f"Child window tittle {driver.title}")
# driver.switch_to.window(Parent_window)

# using loop
for window in windowsID:
    driver.switch_to.window(window)
    print(driver.title)
driver.quit()
