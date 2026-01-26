import sys
sys.path.append(".")
from utils import pet_payloads

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

def test_pet_get_deleted_valid(setup_environment):
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

def test_pet_post_valid(setup_environment):
    session, pet_payload = setup_environment
    response = session.post(f"{session.base_url}/pet", json=pet_payloads.pet_payload_post_test)
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == pet_payloads.pet_payload_post_test['id']
    assert response.json()['name'] == pet_payloads.pet_payload_post_test['name']
    assert response.json()['status'] == pet_payloads.pet_payload_post_test['status']

def test_pet_update_valid(setup_environment):
    session, pet_payload = setup_environment
    updated_payload = pet_payload.copy()
    updated_payload['name'] = "UpdatedTestPet"
    updated_payload['status'] = "sold"
    response = session.put(f"{session.base_url}/pet", json=updated_payload)
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == updated_payload['id']
    assert response.json()['name'] == updated_payload['name']
    assert response.json()['status'] == updated_payload['status']