class TestApi:
    def test_fetch_markets(self, client):
        response = client.get("/markets")
        assert response.status_code == 200
        assert response.json()

    def test_fetch_orders(self, client):
        response = client.get("/orders")
        assert response.status_code == 200
        assert response.json()

    def test_fetch_order(self, client):
        order_id = "order_id_1"
        pair = "BTC/USDT"
        response = client.get(f"/order?id={order_id}&pair={pair}")
        assert response.status_code == 200
        assert response.json()

    def test_create_order(self, client):
        payload = {
            "pair": "BTC/USDT",
            "type": "limit",
            "side": "buy",
            "price": 50000.0,
            "amount": 0.1,
        }
        response = client.post("/order", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["symbol"] == payload["pair"]
        assert response_json["type"] == payload["type"]
        assert response_json["side"] == payload["side"]
        assert response_json["price"] == payload["price"]
        assert response_json["amount"] == payload["amount"]

    def test_cancel_order(self, client):
        order_id = "order_id_1"
        pair = "BTC/USDT"
        response = client.delete(f"/order?id={order_id}&pair={pair}")
        assert response.status_code == 200
        assert response.json()
        assert response.json()['status'] == 'cancelled'

    def test_fetch_balance(self, client):
        response = client.get("/balance")
        assert response.status_code == 200
        assert response.json()

    def test_fetch_ohlcv(self, client):
        pair = "BTC/USDT"
        timeframe = "1m"
        since = 1234567890
        limit = 100
        response = client.get(f"/ohlcv?pair={pair}&timeframe={timeframe}&since={since}&limit={limit}")
        assert response.status_code == 200
        assert response.json()

    def test_fetch_ticker(self, client):
        pair = "BTC/USDT"
        response = client.get(f"/ticker?pair={pair}")
        assert response.status_code == 200
        assert response.json()

    def test_fetch_leverage_tiers(self, client):
        symbol = "BTC/USDT"
        response = client.get(f"/leverage_tiers?symbols={symbol}")
        assert response.status_code == 200
        assert response.json()

    def test_set_leverage(self, client):
        payload = {
            "pair": "BTC/USDT",
            "leverage": 100,
            "long_leverage": 100,
            "short_leverage": 100,
        }
        response = client.post(f"/leverage", json=payload)
        assert response.status_code == 200
        assert response.json()

    def test_fetch_trades(self, client):
        symbol = "BTC/USDT"
        since = 1234567890
        limit = 100
        response = client.get(f"/trades?symbol={symbol}&since={since}&limit={limit}")
        assert response.status_code == 200
        assert response.json()