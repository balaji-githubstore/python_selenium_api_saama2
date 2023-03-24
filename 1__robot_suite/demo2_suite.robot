*** Settings ***
Library     DateTime

*** Variables ***
${BROWSER_NAME}     chrome
${URL}      https://github.com/login
@{COLORS}       jack    mango   green
&{DIC}      name=bala   mobile=2348934

*** Test Cases ***
TC1
    Log To Console    ${COLORS}[2]
    Log To Console    ${DIC}
    Log To Console    ${DIC}[mobile]
    Log To Console  message=Balaji Dinakaran
    Log To Console    ${EXECDIR}${/}test_data${/}add_pet.json

TC2
    Log To Console    message=Bala
    Log     message=Welcome to robot framework

TC3
    ${my_name}=     Set Variable       Balaji
    Log To Console    ${my_name}

TC4
    ${radius}   Set Variable    10
    #calculate area of circle and print the outpust
    ${result}=       Evaluate    3.14*${radius}*${radius}
    Log To Console    ${result}

    ${expected_result}      Convert To Number    314.0
    Should Be Equal    ${result}    ${expected_result}

TC5
    ${current_date}     Get Current Date
    Log To Console    ${current_date}