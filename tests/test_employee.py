def test_get_employees(client):
    
    response = client.get(
        "/api/v1/employees"
    )

    assert response.status_code in [200, 401]