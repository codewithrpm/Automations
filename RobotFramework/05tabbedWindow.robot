*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TabbedwindowTest
    Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
    Maximize Browser Window
    Set Selenium Speed    1
    Wait Until Element Is Visible    xpath://a[normalize-space()='OrangeHRM, Inc']    10 secs
    Click Link    xpath://a[normalize-space()='OrangeHRM, Inc']

    # Switch to the newly opened tab using Switch Window
    Switch Window    NEW
    Wait Until Element Is Visible    xpath://div[@class='d-flex web-menu-btn']//li[1]//a[1]    10 secs
    Click Element    xpath://div[@class='d-flex web-menu-btn']//li[1]//a[1]

    # Switch back to the original tab (optional)
    Switch Window    index=0

    Close All Browsers

