import pytest

@pytest.mark.crud
@pytest.mark.smoke
def test_pet_get_response_valid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == pet_payload['id']
    assert isinstance(response.json()['id'], int)
    assert isinstance(response.json()['name'], str)
    assert isinstance(response.json()['status'], str)

@pytest.mark.smoke
def test_find_by_status_valid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": pet_payload['status']})
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), list)
    for pet in response.json():
        assert 'status' in pet
        assert pet['status'] == pet_payload['status']