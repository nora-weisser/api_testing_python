import requests

BASIC_URL = "https://www.boredapi.com/api/"
ACTIVITY_API = "activity"


def construct_url(common_url, api):
    return common_url + api


"""
Sunny day test case:
Target API URL: https://www.boredapi.com/api/activity
Perform GET request
Expected status code: 200
"""


def test_get_status_code_equals_200():
    url = construct_url(BASIC_URL, ACTIVITY_API)
    response = requests.get(url)
    assert response.status_code == 200, print(
        "Got wrong status code, expected is: {}, actual is {}".format("200", response.status_code))


"""
Failed day test case:
Target API URL: https://www.boredapi.com/api/activity
Perform GET request
Expected status code: 201
"""


def test_failed_get_status_code_equals_201():
    url = construct_url(BASIC_URL, ACTIVITY_API)
    response = requests.get(url)
    assert response.status_code == 201, print(
        "Got wrong status code, expected is: {}, actual is {}".format("201", response.status_code))


"""
Sunny day test case: Check response-body
Target API URL: https://www.boredapi.com/api/activity?type=relaxation
Perform GET request
Expected "type"  in the response-body: "relaxation"
"""


def test_check_type_in__response_body():
    url = construct_url(BASIC_URL, ACTIVITY_API) + "?type=relaxation"
    response = requests.get(url)
    assert response.json()["type"] == "relaxation", print(
        "Got wrong type in response-body, expected is: {}, actual is {}".format("relaxation", response.json()["type"]))


"""
Sunny day test case:
Target API URL: https://www.boredapi.com/api/activity
Perform GET request
Expected Content-Type property in headers: application/json; charset=utf-8
"""


def test_check_content_type_headers():
    url = construct_url(BASIC_URL, ACTIVITY_API)
    response = requests.get(url)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8", print(
        "Got wrong content type in headers, expected is: {}, actual is {}".format("application/json; charset=utf-8",
                                                                                  response.headers["Content-Type"]))
