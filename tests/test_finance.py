def test_finance(client):
    
    response = client.get(
        "/api/v1/finance"
    )

    assert response.status_code in [200,401]