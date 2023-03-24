*** Settings ***
Library     DateTime

*** Test Cases ***
TC1
    Log To Console  message=Balaji Dinakaran

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