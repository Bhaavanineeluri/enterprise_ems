def test_get_companies(client):
    
    response = client.get(
        "/api/v1/company"
    )

    assert response.status_code in [200, 401]