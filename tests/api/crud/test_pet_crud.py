import sys
sys.path.append(".")
from utils import pet_payloads
import pytest

@pytest.mark.crud
@pytest.mark.smoke
def test_pet_get_response_valid(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == pet_payload['id']
    assert isinstance(response.json()['id'], int)
    assert isinstance(response.json()['name'], str)
    assert isinstance(response.json()['status'], str)

@pytest.mark.crud
def test_pet_get_deleted(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    delete_response = session.delete(f"{session.base_url}/pet/{pet_payload['id']}")
    assert delete_response.status_code == 200
    get_response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")
    assert get_response.status_code == 404

@pytest.mark.crud
def test_pet_delete(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    delete_response = session.delete(f"{session.base_url}/pet/{pet_payload['id']}")
    assert delete_response.status_code == 200

@pytest.mark.crud
def test_pet_post_valid(setup_environment):
    session  = setup_environment
    response = session.post(f"{session.base_url}/pet", json=pet_payloads.pet_payload_post_test)
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == pet_payloads.pet_payload_post_test['id']
    assert response.json()['name'] == pet_payloads.pet_payload_post_test['name']
    assert response.json()['status'] == pet_payloads.pet_payload_post_test['status']

@pytest.mark.crud
def test_pet_update_valid(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    updated_payload = pet_payload.copy()
    updated_payload['name'] = pet_payloads.pet_payload_updated["name"]
    updated_payload['status'] = pet_payloads.pet_payload_post_test["status"]
    response = session.put(f"{session.base_url}/pet", json=updated_payload)
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == updated_payload['id']
    assert response.json()['name'] == updated_payload['name']
    assert response.json()['status'] == updated_payload['status']

@pytest.mark.crud
@pytest.mark.edge
def test_delete_pet_twice(setup_environment, pet):
    session = setup_environment
    pet_payload = pet
    delete_response = session.delete(f"{session.base_url}/pet/{pet_payload["id"]}")
    assert delete_response.status_code == 200
    delete_response = session.delete(f"{session.base_url}/pet/{pet_payload["id"]}")
    assert delete_response.status_code == 404