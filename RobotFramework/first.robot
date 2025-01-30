*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Test Cases ***
Login Operation
    Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
    Wait Until Element Is Visible    name:username    10 seconds
    Input Text    name:username    Admin
    Wait Until Element Is Visible    name:password    10 seconds
    Input Text    name:password    admin123
    Wait Until Element Is Visible    xpath://button[normalize-space()='Login']    10 seconds
    Click Button    xpath://button[normalize-space()='Login']
    Close Browser
