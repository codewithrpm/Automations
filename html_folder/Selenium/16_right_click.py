from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(10)

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
action = ActionChains(driver)
# For right click using  context_click
action.context_click(button).perform()
driver.quit()