import pytest
import allure

@allure.feature("Pet API")
@allure.story("Find pet by status of empty value")
@allure.title("Should receive error code")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.edge
@pytest.mark.xfail(reason="API does not validate empty status parameter properly")
def test_find_by_status_empty(setup_environment):
    session = setup_environment

    with allure.step("Send GET request with empty status"):
        response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": ""})

    with allure.step("Verify validation error is returned"):
        assert response.status_code == 400

@allure.feature("Pet API")
@allure.story("Post pet with ID value NULL")
@allure.title("Should receive error code")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.edge
@pytest.mark.xfail(reason="API does not validate empty ID parameter properly, returns pet with ID 9223372016900022292")
def test_post_pet_empty_id(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    invalid_payload = pet_payload.copy()
    invalid_payload['id'] = None

    with allure.step("Send POST request with NULL ID"):
        response = session.post(f"{session.base_url}/pet", json=invalid_payload)

    with allure.step("Verify validation error is returned"):
        assert response.status_code == 400

@allure.feature("Pet API")
@allure.story("Post pet with ID value -1")
@allure.title("Should receive error code")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.edge
@pytest.mark.xfail(reason="API does not validate empty ID parameter properly, returns pet with ID 9223372036854022456")
def test_post_pet_negative_id_value(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    invalid_payload = pet_payload.copy()
    invalid_payload['id'] = -1

    with allure.step("Send POST request with negative ID"):
        response = session.post(f"{session.base_url}/pet", json=invalid_payload)

    with allure.step("Verify validation error is returned"):
        assert response.status_code == 400

@allure.feature("Pet API")
@allure.story("Get non-existent pet")
@allure.title("Should delete pet and receive error message after get request")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.edge
def test_pet_get_deleted(setup_environment, pet):
    session = setup_environment
    pet_payload = pet

    with allure.step("Send DELETE request"):
        delete_response = session.delete(f"{session.base_url}/pet/{pet_payload['id']}")
    
    with allure.step("Verify response status"):
        assert delete_response.status_code == 200
    
    with allure.step("Send GET request"):
        get_response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")
    
    with allure.step("Verify response status code"):
        assert get_response.status_code == 404