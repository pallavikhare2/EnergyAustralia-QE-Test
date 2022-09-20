import requests
import pytest
import json
def test_get_employee_details_check_status_code_equals_200():
    response = requests.get("https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals")
     #print (response.status_code)
    print (response)
     #assert response.status_code == 201
    if response.ok:
        print("Response code is 200 and it is expected response")
        print("**************************")
        response_body = response.json()
        print(response_body)
        l1= len(response_body)
        if l1>0:
            print("**************************")
            print(l1)
            print("**************************")
            print(response_body[0])
            print("**************************")
                #print (len(response_body[0]['bands'][0]))
            l = (len(response_body[0]['bands']))
            print (len(response_body[0]['bands']))
            print("**************************")
            #print (len(response_body[0]['bands'][0]))
            print ((response_body[0]['bands'][0]))
            print ("****************")
            print ((response_body[0]['bands'][0]['name']))
            print ((response_body[0]['bands'][1]))
            print ((response_body[0]['bands'][2]))
            print ((response_body[0]['bands'][3]))
            #print ((response_body[0]['bands'][0]))
            #print ((response_body[0]['bands'][1]))
        else:
            print("Status code is 200 but received empty json response ")

    else:
        print("Error response received from the server with status code "+ str(response.status_code) )

test_get_employee_details_check_status_code_equals_200()
