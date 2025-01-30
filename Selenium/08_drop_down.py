from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//a[normalize-space()='Create new account']").click()

month = driver.find_element(By.ID,"month")
drop_month = Select(month)
dropDown_list = drop_month.options
print(f"The length of the list are {len(dropDown_list)}")
# drop_month.select_by_visible_text("Sep")
time.sleep(3)
for lists in dropDown_list:
    print(lists.text)

# select the month from drop down without using built-in functions
for lists in dropDown_list:
    if lists.text == "Sep":
        lists.click()

driver.quit()