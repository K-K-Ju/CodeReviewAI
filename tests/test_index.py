from fastapi.testclient import TestClient
from codereviewai import main

test_client = TestClient(main.app)

def test_index_get():
    resp_status_code = test_client.get('/api/v1/').status_code
    assert resp_status_code == 200

def test_index_post_404():
    resp_status_code = test_client.post('/api/v1/').status_code
    assert resp_status_code == 405
