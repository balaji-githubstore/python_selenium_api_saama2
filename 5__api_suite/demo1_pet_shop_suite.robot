*** Settings ***
Library     RequestsLibrary
Library    OperatingSystem

*** Test Cases ***
TC1 GET VALID PET
    ${pet_id}     Set Variable      61017777

    Create Session    alias=petshop    url=https://petstore.swagger.io/v2

    ${response}     GET On Session      alias=petshop   url=/pet/${pet_id}      expected_status=200
    Log     ${response}
    Log     ${response.json()}
    Status Should Be    expected_status=200

    Log To Console    ${response.json()}[id]
    Log To Console    ${response.json()}[name]

TC2 Add pet
    ${body}     Get Binary File     ${EXECDIR}${/}test_data${/}add_pet.json
    &{head}     Create Dictionary       Content-Type=application/json       Connection=keep-alive
    Create Session    alias=petshop    url=https://petstore.swagger.io/v2
    ${response}     POST On Session     alias=petshop   url=/pet        headers=${head}     data=${body}
    Log     ${response}
    Log     ${response.json()}
    Status Should Be    expected_status=200