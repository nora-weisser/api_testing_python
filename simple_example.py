import requests

BASIC_URL = "https://www.boredapi.com/api/"
ACTIVITY_API = "activity"

def construct_url(common_url, api):
    return common_url + api

def test_get_status_code_equals_200(common_url, api):
    url = construct_url(common_url, api)
    response = requests.get(url)
    try:
        assert response.status_code == 200
        print("Everything is alright")
    except AssertionError:
        print("Got the wrong status code")


if __name__ == "__main__":
    test_get_status_code_equals_200(BASIC_URL, ACTIVITY_API)