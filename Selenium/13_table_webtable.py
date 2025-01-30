from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Count number of rows and columns from a table

# //table[@name='BookTable']/tbody/tr or //table[@name='BookTable']//tr , we can write this way
# To find rows in a table

no_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
no_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))

print(f"Number of rows in this webtable are {no_of_rows}")
print(f"Number of columns in this webtable are {no_of_columns}")

# Read specific row and column data

data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(f"Fifth row's first column's data : {data}")

# Read all rows and columns data
print(f"Printing all the rows and columns data.!")
for row in range(2,no_of_rows+1):
    for column in range(1,no_of_columns+1):
        data = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[{column}]").text
        print(data,end="            ")
    print()

# Read data based on conditions(List book name whose author is Mukesh)
print(f"--- printing Book name which is written by Mukesh ---")
for r in range(2,no_of_rows+1):
    authorName = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[1]").text
        price = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[4]").text
        print(f"Author Name is : {authorName} and Book name is {bookName} and Price : {price}")

driver.quit()