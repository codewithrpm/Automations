*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
HandlingAlert
    Open Browser    https://testautomationpractice.blogspot.com/    chrome
    Maximize Browser Window
    Set Selenium Speed    10
    # Click Element    xpath://button[@id='alertBtn']
    # Handle Alert    accept
    # Keep open alert using this below cmd
    # Handle Alert    leave
    Click Element    xpath://button[@id='promptBtn']
    Alert Should Be Present    Please enter your name:
    Execute JavaScript    window.promptResponse = "Rupam"; window.prompt = () => window.promptResponse;
    Handle Alert    accept
    Close Browser


