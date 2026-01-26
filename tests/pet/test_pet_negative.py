
import pytest

def test_pet_response_invalid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/0")
    assert response.status_code == 404
    assert 'application/json' in response.headers['Content-Type']
    assert response.json()['code'] == 1
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'Pet not found'

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


@pytest.mark.xfail(reason="API does not validate invalid ID parameter properly, Server errors occur instead of proper 400 responses")
def test_post_pet_invalid_id_type(setup_environment):
    session, pet_payload = setup_environment
    invalid_payload = pet_payload.copy()
    invalid_payload['id'] = "abc"
    response = session.post(f"{session.base_url}/pet", json=invalid_payload)
    assert response.status_code == 400

@pytest.mark.xfail(reason="API does not validate empty ID parameter properly, returns pet with ID 9223372016900022292")
def test_post_pet_empty_id(setup_environment):
    session, pet_payload = setup_environment
    invalid_payload = pet_payload.copy()
    invalid_payload['id'] = None
    response = session.post(f"{session.base_url}/pet", json=invalid_payload)
    assert response.status_code == 400

@pytest.mark.xfail(reason="API does not validate empty ID parameter properly, returns pet with ID 9223372036854022456")
def test_post_pet_negative_id_value(setup_environment):
    session, pet_payload = setup_environment
    invalid_payload = pet_payload.copy()
    invalid_payload['id'] = -1
    response = session.post(f"{session.base_url}/pet", json=invalid_payload)
    assert response.status_code == 400

