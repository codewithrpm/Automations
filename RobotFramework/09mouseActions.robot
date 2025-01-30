*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
mouseActions
    # Right click
    Open Browser    https://swisnl.github.io/jQuery-contextMenu/demo.html    chrome
    Maximize Browser Window
    Open Context Menu    xpath://span[@class='context-menu-one btn btn-neutral']
    Sleep    3

    # Double click actions
    Go To    https://testautomationpractice.blogspot.com/
    Maximize Browser Window
    Double Click Element    xpath://button[normalize-space()='Copy Text']
    Sleep    3
    # Drag and Drop
    Drag And Drop    xpath://div[@id='draggable']    xpath://div[@id='droppable']
    Sleep    3
    Close All Browsers
    