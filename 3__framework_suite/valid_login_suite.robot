*** Settings ***
Documentation       This suite file contains test case related
...     to valid login

Resource    ../4__keywords/CommonFunctionalities.resource

Test Setup      Open Browser And Navigate To URL
Test Teardown       Close Browser

Test Template       Verify Valid Login Template

*** Test Cases ***
TC1    physician    physician   Dutch   OpenEMR
TC2    accountant    accountant   Dutch   OpenEMR



*** Keywords ***
Verify Valid Login Template
    [Arguments]     ${username}     ${password}     ${language}     ${expected_title}
    Input Text    id=authUser     ${username}
    Input Password    id=clearPass    ${password}
    Select From List By Label    xpath=//select[@name='languageChoice']     ${language}
    Click Element    id=login-button
    Title Should Be    ${expected_title}

