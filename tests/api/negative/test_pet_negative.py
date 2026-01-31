import sys
sys.path.append(".")
import pytest
from utils import pet_payloads
import allure

@allure.feature("Pet API")
@allure.story("Get pet with ID = 0")
@allure.title("Should receive error message")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
def test_pet_response_invalid(setup_environment):
    session = setup_environment

    with allure.step("Send GET request with ID = 0"):
        response = session.get(f"{session.base_url}/pet/{pet_payloads.pet_payload_invalid['id']}")
    
    with allure.step("Verify response status and headers"):
        assert response.status_code == 404
        assert 'application/json' in response.headers['Content-Type']

    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), dict)
    
    with allure.step("Verify error message content"):
        assert response.json()['code'] == 1
        assert response.json()['type'] == 'error'
        assert response.json()['message'] == 'Pet not found'

@allure.feature("Pet API")
@allure.story("Get pet with status of invalid value")
@allure.title("Should receive empty json")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
def test_find_by_status_invalid(setup_environment):
    session = setup_environment

    with allure.step("Send GET request with invalid status value"):
        response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": pet_payloads.pet_payload_invalid['status']})

    with allure.step("Verify response status and headers"):
        assert response.status_code == 200
        assert 'application/json' in response.headers['Content-Type']

    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), list)
    
    with allure.step("Verify response is empty"):
        assert len(response.json()) == 0

@allure.feature("Pet API")
@allure.story("Post pet with ID of type string")
@allure.title("Should receive invalid input error message")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
@pytest.mark.xfail(reason="API does not validate invalid ID parameter properly, Server errors occur instead of proper 400 responses")
def test_post_pet_invalid_id_type(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    invalid_payload = pet_payload.copy()
    invalid_payload['id'] = "abc"

    with allure.step("Send POST request with ID of type string"):
        response = session.post(f"{session.base_url}/pet", json=invalid_payload)

    with allure.step("Verify validation error is returned"):
        assert response.status_code == 400