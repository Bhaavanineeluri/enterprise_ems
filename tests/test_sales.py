def test_sales(client):
    
    response = client.get(
        "/api/v1/sales/quotations"
    )

    assert response.status_code in [200, 401]