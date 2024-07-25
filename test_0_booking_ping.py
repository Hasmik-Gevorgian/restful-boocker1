import requests
import pytest
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Booking Feature")
@allure.suite("Ping Tests")
@allure.title("Health Check Endpoint Test")
@allure.description("This test checks the health of the API by calling the /ping endpoint.")
@allure.severity(allure.severity_level.CRITICAL)
def test_health_check():
    with allure.step("Send GET request to health check endpoint"):
        response = requests.get('https://restful-booker.herokuapp.com/ping')

    with allure.step("Verify the response status code is 201"):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'
