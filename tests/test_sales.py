def test_sales(client):
    
    response = client.get(
        "/api/v1/sales"
    )

    assert response.status_code in [200,401]