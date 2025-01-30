*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
switchBrowser
    Open Browser    https://www.flipkart.com/    chrome
    Maximize Browser Window
    Sleep    3

    Open Browser    https://www.meesho.com/    chrome
    Maximize Browser Window
    Sleep    3
    
    Switch Browser    1
    ${title1} =    Get Title
    Log To Console    ${title1}
    
    Switch Browser    2
    ${title2} =    Get Title
    Log To Console    ${title2}
    Sleep    2
    Close All Browsers