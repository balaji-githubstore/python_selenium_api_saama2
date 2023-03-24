*** Settings ***
Documentation   This file will contains browser configuration

Library     SeleniumLibrary     run_on_failure=None

*** Variables ***
${BROWSER_NAME}     chrome
${URL}      https://demo.openemr.io/b/openemr

*** Keywords ***
Open Browser And Navigate To URL
    Open Browser    browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=${URL}