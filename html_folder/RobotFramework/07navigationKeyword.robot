*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
navigationTest
    Open Browser    https://www.google.com/    chrome
    Maximize Browser Window
    ${location} =    Get Location
    Log To Console    ${location}
    Sleep    2

    Go To    https://www.bing.com/
    Maximize Browser Window
    ${location} =    Get Location
    Log To Console    ${location}
    Sleep    2

    Go Back
    Maximize Browser Window
    ${location} =    Get Location
    Log To Console    ${location}
    Sleep    2

    Close Browser
