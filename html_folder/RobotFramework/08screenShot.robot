*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
screenShot
    Open Browser    https://www.google.com/    chrome
    Maximize Browser Window

    Capture Element Screenshot    //img[@alt='Google']    logo.png
    Capture Page Screenshot    fullPage.png
    Close Browser