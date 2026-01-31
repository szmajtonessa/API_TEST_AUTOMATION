import sys
sys.path.append(".")
from utils import pet_payloads
import pytest
import allure

@allure.feature("Pet API")
@allure.story("Get Pet")
@allure.title("Should receive json of pet parameters for existing pet ID")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.crud
@pytest.mark.smoke
def test_pet_get_response_valid(setup_environment, pet):
    session = setup_environment
    pet_payload = pet

    with allure.step("Send GET request"):
        response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")

    with allure.step("Verify response status and headers"):
        assert response.status_code == 200
        assert 'application/json' in response.headers['Content-Type']
    
    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), dict)
    
    with allure.step("Verify response ID is as inquired"):
        assert response.json()['id'] == pet_payload['id']

    with allure.step("Verify response parameters are of proper type"):
        assert isinstance(response.json()['id'], int)
        assert isinstance(response.json()['name'], str)
        assert isinstance(response.json()['status'], str)



@allure.feature("Pet API")
@allure.story("Delete pet")
@allure.title("Should delete pet from database")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.crud
def test_pet_delete(setup_environment, pet):
    session = setup_environment
    pet_payload = pet

    with allure.step("Send DELETE request"):
        delete_response = session.delete(f"{session.base_url}/pet/{pet_payload['id']}")

    with allure.step("Verify response status"):
        assert delete_response.status_code == 200

@allure.feature("Pet API")
@allure.story("Create pet")
@allure.title("Should create pet with valid payload")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.crud
def test_pet_post_valid(setup_environment):
    session  = setup_environment

    with allure.step("Send POST request"):
        response = session.post(f"{session.base_url}/pet", json=pet_payloads.pet_payload_post_test)

    with allure.step("Verify response status and headers"):
        assert response.status_code == 200
        assert 'application/json' in response.headers['Content-Type']

    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), dict)
    
    with allure.step("Verify response parameters are of proper type"):
        assert response.json()['id'] == pet_payloads.pet_payload_post_test['id']
        assert response.json()['name'] == pet_payloads.pet_payload_post_test['name']
        assert response.json()['status'] == pet_payloads.pet_payload_post_test['status']



@allure.feature("Pet API")
@allure.story("Update pet")
@allure.title("Should update a pet object with valid payload")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.crud
def test_pet_update_valid(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    updated_payload = pet_payload.copy()
    updated_payload['name'] = pet_payloads.pet_payload_updated['name']
    updated_payload['status'] = pet_payloads.pet_payload_post_test['status']

    with allure.step("Send PUT request"):
        response = session.put(f"{session.base_url}/pet", json=updated_payload)

    with allure.step("Verify response status and headers"):
        assert response.status_code == 200
        assert 'application/json' in response.headers['Content-Type']

    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), dict)
    
    with allure.step("Verify response parameters are of proper type"):
        assert response.json()['id'] == updated_payload['id']
        assert response.json()['name'] == updated_payload['name']
        assert response.json()['status'] == updated_payload['status']

@allure.feature("Pet API")
@allure.story("Delete non-existent pet")
@allure.title("Should delete pet once, then receive error message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.crud
@pytest.mark.edge
def test_delete_pet_twice(setup_environment, pet):
    session = setup_environment
    pet_payload = pet

    with allure.step("Send DELETE request"):
        delete_response = session.delete(f"{session.base_url}/pet/{pet_payload['id']}")

    with allure.step("Verify response status"):
        assert delete_response.status_code == 200

    with allure.step("Send another DELETE request"):
        delete_response = session.delete(f"{session.base_url}/pet/{pet_payload['id']}")
    
    with allure.step("Verify response status"):
        assert delete_response.status_code == 404