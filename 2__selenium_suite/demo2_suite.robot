*** Settings ***
Library     SeleniumLibrary



Test Setup  Open Browser And Navigate To URL
Test Teardown   Close Browser

*** Variables ***
${BROWSER_NAME}     chrome
${URL}      https://github.com/login


*** Keywords ***
Open Browser And Navigate To URL
    Open Browser    browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=${URL}

*** Test Cases ***
TC1
    [Tags]      UI
    Element Text Should Be    xpath=//h1    Sign in to GitHub


TC2
    [Tags]  login    high     smoke
    Input Text    id=login_field    dina
    Input Password    id=password    welcome123
    Click Element    name=commit
#    Element Text Should Be    xpath=//*[contains(text(),'Incorrect')]    Incorrect username or password.
    Element Should Contain    xpath=//*[contains(text(),'Incorrect')]    Incorrect username or password