import pytest
import requests
import sys
sys.path.append(".")
from utils import pet_payloads
from utils import helpers
import copy

@pytest.fixture(scope="session")
def setup_environment():
    s = helpers.APISession()
    s.base_url = helpers.URLS["base_url"]
    s.headers.update({'api-key': 'special-key'})

    yield s
    s.close()

@pytest.fixture
def pet(setup_environment):
    pet_payload = copy.deepcopy(pet_payloads.pet_payload)

    response = setup_environment.post(f"{setup_environment.base_url}/pet", json=pet_payload)

    assert response.status_code == 200

    yield pet_payload

    setup_environment.delete(f"{setup_environment.base_url}/pet/{pet_payload['id']}")
