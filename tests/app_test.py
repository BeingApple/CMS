
def test_customer_list(flask_client):
    resp = flask_client.get('/customer_list/')
    assert resp.status_code == 200


def test_customer_list_page(flask_client):
    resp = flask_client.get('/customer_list/30/')
    assert resp.status_code == 200
