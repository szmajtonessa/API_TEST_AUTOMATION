import sys
sys.path.append(".")
from utils import pet_payloads
from jsonschema import validate
from schemas import schemas
import pytest

@pytest.mark.contract
def test_pet_get_schema(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/{pet_payload["id"]}")
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    response_json = response.json()
    validate(instance=response_json, schema=schemas.pet_response_schema)

@pytest.mark.contract
def test_find_by_status_schema(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": pet_payload['status']})
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), list)
    response_json = response.json()
    for pet in response_json:
        validate(instance=response_json, schema=schemas.pet_response_schema)

@pytest.mark.contract
def test_pet_post_schema(setup_environment):
    session, pet_payload = setup_environment
    response = session.post(f"{session.base_url}/pet", json=pet_payloads.pet_payload_post_test)
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    assert isinstance(response.json(), dict)
    response_json = response.json()
    validate(instance=response_json, schema=schemas.pet_response_schema)