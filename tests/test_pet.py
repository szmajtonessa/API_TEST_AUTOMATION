
def test_pet_response_valid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json()['id'] == pet_payload['id']
    assert isinstance(response.json()['id'], int)
    assert isinstance(response.json()['name'], str)
    assert isinstance(response.json()['status'], str)
    

def test_pet_response_invalid(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/0")
    assert response.status_code == 404
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json()['code'] == 1
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'Pet not found'


def test_pet_get_deleted(setup_environment):
    session, pet_payload = setup_environment
    delete_response = session.delete(f"{session.base_url}/pet/{pet_payload['id']}")
    assert delete_response.status_code == 200
    get_response = session.get(f"{session.base_url}/pet/{pet_payload['id']}")
    assert get_response.status_code == 404

def test_find_by_status(setup_environment):
    session, pet_payload = setup_environment
    response = session.get(f"{session.base_url}/pet/findByStatus", params={"status": '?status=' + pet_payload['status']})
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert any(response.json()[i]['id'] == pet_payload['id'] for i in range(len(response.json())))
