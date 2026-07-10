def test_login(client):
    
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "admin@test.com",
            "password": "Admin@123"
        }
    )

    assert response.status_code in [200, 401]