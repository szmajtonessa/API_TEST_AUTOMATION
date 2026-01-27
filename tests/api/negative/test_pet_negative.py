import sys
sys.path.append(".")
import pytest
from utils import pet_payloads

@pytest.mark.negative
def test_pet_response_invalid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/{pet_payloads.pet_payload_invalid["id"]}")
    assert response.status_code == 404
    assert 'application/json' in response.headers['Content-Type']
    assert response.json()['code'] == 1
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'Pet not found'

@pytest.mark.negative
def test_find_by_status_invalid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": pet_payloads.pet_payload_invalid["status"]})
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0

@pytest.mark.negative
@pytest.mark.xfail(reason="API does not validate invalid ID parameter properly, Server errors occur instead of proper 400 responses")
def test_post_pet_invalid_id_type(setup_environment):
    session, pet_payload = setup_environment
    invalid_payload = pet_payload.copy()
    invalid_payload['id'] = "abc"
    response = session.post(f"{session.base_url}/pet", json=invalid_payload)
    assert response.status_code == 400