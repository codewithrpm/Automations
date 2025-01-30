*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}    https://www.techlistic.com/p/selenium-practice-form.html
${browser}    chrome
*** Test Cases ***
HandlingDropDown
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Speed    3

    # Selecting drop down box
    Select From List By Label    continents    Europe
    Select From List By Index    continents    4
    # Select From List By Value    continents    3

    # List box handling
    Select From List By Label    selenium_commands    Navigation Commands



    Close Browser
    