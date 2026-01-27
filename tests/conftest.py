import pytest
import requests
import sys
sys.path.append(".")
from utils import pet_payloads
from utils import helpers

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    s = requests.Session()
    s.base_url = helpers.URLS["base_url"]
    s.headers.update({'api-key': 'special-key'})
    pet_payload = pet_payloads.pet_payload
    s.post(f"{s.base_url}/pet", json=pet_payload)
    yield s, pet_payload
    s.delete(f"{s.base_url}/pet/{pet_payload['id']}")
    s.close()
