from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

admin = driver.find_element(By.XPATH, "//span[text()='Admin']")
user_management = driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
user = driver.find_element(By.XPATH, "//ul[@role='menu']//li")

action = ActionChains(driver)
action.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()
time.sleep(3)
driver.quit()