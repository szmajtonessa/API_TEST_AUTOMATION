import pytest
import requests
import sys
sys.path.append(".")
from utils import pet_payloads
from utils import helpers
import copy

# @pytest.fixture(scope="session", autouse=True)
# def setup_environment():
#     s = requests.Session()
#     s.base_url = helpers.URLS["base_url"]
#     s.headers.update({'api-key': 'special-key'})
#     pet_payload = pet_payloads.pet_payload
#     s.post(f"{s.base_url}/pet", json=pet_payload)
#     yield s, pet_payload
#     s.delete(f"{s.base_url}/pet/{pet_payload['id']}")
#     s.close()
@pytest.fixture(scope="session")
def setup_environment():
    s = requests.Session()
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
