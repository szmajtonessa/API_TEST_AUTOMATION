import pytest
import allure

@allure.feature("Pet API")
@allure.story("Get Pet")
@allure.title("Should receive json of pet parameters")
@allure.severity(allure.severity_level.BLOCKER)
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
@allure.story("Find pets by status of valid value")
@allure.title("Should receive a list of pets of inquired status")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_find_by_status_valid(setup_environment, pet):
    session = setup_environment
    pet_payload = pet

    with allure.step("Send GET request"):
        response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": pet_payload['status']})

    with allure.step("Verify response status and headers"):
        assert response.status_code == 200
        assert 'application/json' in response.headers['Content-Type']

    with allure.step("Verify response body is a json object"):
        assert isinstance(response.json(), list)

    with allure.step("Verify returned pet objects are of inquired status"):
        for pet in response.json():
            assert 'status' in pet
            assert pet['status'] == pet_payload['status']