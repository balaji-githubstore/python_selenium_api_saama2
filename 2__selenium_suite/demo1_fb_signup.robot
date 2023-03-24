*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC1 Register
    Open Browser    browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://www.facebook.com/
    Click Element   link:Create new account
    Input Text    name=firstname    Bala
    Input Text    name=lastname    dina
    Input Password    id=password_step_input    welcome123
    Select From List By Label    id=day         25
    Select From List By Value    id=month    12
    Select From List By Label    xpath=//select[@title='Year']  2001
    Click Element    xpath=//label[text()='Custom']
    #below teardown runs always
    [Teardown]  Close Browser


    
