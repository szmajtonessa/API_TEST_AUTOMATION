
import pytest


def test_pet_response_valid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == pet_payload['id']
    assert isinstance(response.json()['id'], int)
    assert isinstance(response.json()['name'], str)
    assert isinstance(response.json()['status'], str)
    

def test_pet_response_invalid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/0")
    assert response.status_code == 404
    assert 'application/json' in response.headers['Content-Type']
    assert response.json()['code'] == 1
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'Pet not found'


def test_pet_get_deleted(setup_environment):
    session, pet_payload = setup_environment
    delete_response = session.delete(f"{session.base_url}/pet/{pet_payload['id']}")
    assert delete_response.status_code == 200
    get_response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")
    assert get_response.status_code == 404

def test_find_by_status_valid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": pet_payload['status']})
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), list)
    for pet in response.json():
        assert 'status' in pet
        assert pet['status'] == pet_payload['status']

@pytest.mark.contract
@pytest.mark.xfail(reason="API does not validate empty status parameter properly")
def test_find_by_status_empty(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": ""})
    assert response.status_code == 400

def test_find_by_status_invalid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": "invalid_status"})
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0