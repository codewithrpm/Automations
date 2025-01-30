*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}    https://www.techlistic.com/p/selenium-practice-form.html
${browser}    chrome

*** Test Cases ***
RadioButtonValidation
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Speed    4

    #Selecting radio button
    Select Radio Button    sex    Male
    Select Radio Button    exp    5
    Select Checkbox    Manual Tester
    Unselect Checkbox    Manual Tester
    Select Checkbox    Automation Tester
    Close Browser