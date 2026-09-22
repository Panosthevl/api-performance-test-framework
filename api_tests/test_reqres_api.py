import pytest

def test_get_users_list(api_context):
    response = api_context.get("/api/users?page=2")

    assert response.ok
    assert response.status == 200

    response_json = response.json()

    assert "page" in response_json
    assert "data" in response_json
    assert isinstance(response_json["data"],list)

    assert len(response_json["data"]) > 0

def test_create_new_user(api_context):
    payload = {
        "name":"Panagiotis",
        "job": "QA Engineer"
    }

    response = api_context.post("/api/users",data=payload)

    assert response.status == 201

    response_json = response.json()
    assert response_json["name"] == payload["name"]
    assert response_json["job"] == payload["job"]
    assert "id" in response_json
    assert "createdAt" in response_json

def test_delete_user(api_context):
    """3. DELETE Request: Διαγραφή χρήστη και έλεγχος Empty Response"""
    response = api_context.delete("/api/users/2")
    
    assert response.status == 204

    assert response.text() == ""
