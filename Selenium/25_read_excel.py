import openpyxl

path = "D:\\Automation\\Selenium\\OnePlus_Phones.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook["OnePlus Data"]