def test_finance(client):
    response = client.get("/api/v1/finance/ledgers")
    assert response.status_code in [200, 401]