from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_record():
    response = client.post("/records", json={"id": 1, "data": "test data"}, headers={"Authorization": "Bearer fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "data": "test data"}

def test_get_record():
    response = client.get("/records/1", headers={"Authorization": "Bearer fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "data": "test data"}

def test_update_record():
    response = client.put("/records/1", json={"id": 1, "data": "updated data"}, headers={"Authorization": "Bearer fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "data": "updated data"}

def test_delete_record():
    response = client.delete("/records/1", headers={"Authorization": "Bearer fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"message": "Record deleted successfully"}

def test_list_records():
    response = client.get("/records", headers={"Authorization": "Bearer fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == []
