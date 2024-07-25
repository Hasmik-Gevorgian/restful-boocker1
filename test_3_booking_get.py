import pytest
import requests
import allure

import test_2_booking_post


@pytest.mark.regression
@allure.feature("Booking Feature")
@allure.suite("GET Booking Suite")
@allure.title("Get All Bookings Test")
@allure.description("This test fetches all bookings and verifies the response.")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_booking_all():
    with allure.step("Send GET request to fetch all bookings"):
        response = requests.get('https://restful-booker.herokuapp.com/booking')

    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step("Verify the response contains a list of bookings"):
        assert len(response.json()) > 0, 'The list should not be empty'


@pytest.mark.regression
@allure.feature("Booking Feature")
@allure.suite("GET Booking Suite")
@allure.title("Get Booking By ID Test")
@allure.description("This test fetches a booking by ID and verifies the response.")
@allure.severity(allure.severity_level.CRITICAL)
def test_booking_by_id():
    with allure.step(f"Send GET request to get booking by ID "):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}')

    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step("Verify the response contains 'firstname'"):
        assert 'firstname' in response_data, "The response does not contain 'firstname'"

    with allure.step("Verify the response contains 'lastname'"):
        assert 'lastname' in response_data, "The response does not contain 'lastname'"

    with allure.step("Verify the response contains 'totalprice'"):
        assert 'totalprice' in response_data, "The response does not contain 'totalprice'"

    with allure.step("Verify the response contains 'depositpaid'"):
        assert 'depositpaid' in response_data, "The response does not contain 'depositpaid'"

    with allure.step("Verify the response contains 'bookingdates'"):
        assert 'bookingdates' in response_data, "The response does not contain 'bookingdates'"

    with allure.step("Verify the response contains 'checkin' date"):
        assert 'checkin' in response_data['bookingdates'], "The response does not contain 'checkin'"

    with allure.step("Verify the response contains 'checkout' date"):
        assert 'checkout' in response_data['bookingdates'], "The response does not contain 'checkout'"

    with allure.step("Verify the response contains 'additionalneeds'"):
        assert 'additionalneeds' in response_data, "The response does not contain 'additionalneeds'"

    with allure.step('Verify the value of "depositpaid" is boolean'):
        assert response_data['depositpaid'] is True or response_data['depositpaid'] is False, 'ERRORRR depositpaid'

    with allure.step("Verify 'totalprice' value is an integer or float"):
        assert isinstance(response_data['totalprice'], (int, float)), 'The totalprice value should be an integer or float'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)