*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${browser}    chrome
${url}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
*** Test Cases ***
InputBoxValidation
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Title Should Be    OrangeHRM
    Wait Until Element Is Visible    name:username    10 seconds
    #Create a variable
    ${username_text}    Set Variable    name:username
    
    Element Should Be Visible    ${username_text}
    Element Should Be Enabled    ${username_text}

    Input Text    ${username_text}    rupamc@gmail.com
    Sleep    5
    Clear Element Text    ${username_text}
    Sleep    5
    Close All Browsers
