import sys
sys.path.append(".")
from utils import pet_payloads
from jsonschema import validate
from schemas import schemas
import pytest
import allure

@allure.feature("Pet API")
@allure.story("Check GetByID request response schema")
@allure.title("Should check if response is of expected schema")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.contract
def test_pet_get_schema(setup_environment, pet):
    session = setup_environment
    pet_payload = pet

    with allure.step("Send GET request"):
        response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")

    with allure.step("Verify response status and headers"):
        assert response.status_code == 200
        assert 'application/json' in response.headers['Content-Type']

    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), dict)

    
    with allure.step("Validate response against pet schema"):
        response_json = response.json()
        validate(instance=response_json, schema=schemas.pet_response_schema)

@allure.feature("Pet API")
@allure.story("Check GetByStatus request response schema")
@allure.title("Should check if response is of expected schema")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.contract
def test_find_by_status_schema(setup_environment, pet):
    session = setup_environment
    pet_payload = pet

    with allure.step("Send GET request"):
        response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": pet_payload['status']})
    
    with allure.step("Verify response status and headers"):
        assert response.status_code == 200
        assert 'application/json' in response.headers['Content-Type']

    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), list)

    with allure.step("Validate response against pet schema"):
        response_json = response.json()
        for pet in response_json:
            validate(instance=response_json, schema=schemas.pet_response_schema)

@allure.feature("Pet API")
@allure.story("Check POST request response schema")
@allure.title("Should check if response is of expected schema")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.contract
def test_pet_post_schema(setup_environment):
    session = setup_environment

    with allure.step("Send POST request"):
        response = session.post(f"{session.base_url}/pet", json=pet_payloads.pet_payload_post_test)
    
    with allure.step("Verify response status and headers"):
        assert response.status_code == 200
        assert 'application/json' in response.headers['Content-Type']

    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), dict)

    with allure.step("Validate response against pet schema"):
        response_json = response.json()
        validate(instance=response_json, schema=schemas.pet_response_schema)