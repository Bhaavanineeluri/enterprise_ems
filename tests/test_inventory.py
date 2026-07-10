def test_inventory(client):
    
    response = client.get(
        "/api/v1/inventory"
    )

    assert response.status_code in [200,401]