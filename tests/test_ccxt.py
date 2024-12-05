
def test_describe():
    result = gains.describe()
    assert result
    print(result)

def test_fetch_markets():
    result = gains.fetch_markets()
    assert result
    print(result)


def test_fetch_order():
    result = gains.fetch_order(id="someid", symbol='BTC/USDT')
    assert result
    print(result)

def test_fetch_orders():
    result = gains.fetch_orders(symbol='BTC/USDT', since=1652376700000, limit=100)
    assert result
    print(result)

def test_create_order():
    result = gains.create_order(symbol='BTC/USDT', type="limit", side="buy", amount=1, price=100)
    assert result
    print(result)

def test_cancel_order():
    result = gains.cancel_order(id="someid", symbol='BTC/USDT')
    assert result
    print(result)

def test_fetch_balance():
    result = gains.fetch_balance()
    assert result
    print(result)

def test_fetch_ohlcv():
    result = gains.fetch_ohlcv(symbol='BTC/USDT', timeframe="1m", since=1234567890, limit=100)
    assert result
    print(result)

def test_fetch_ticker():
    result = gains.fetch_ticker(symbol='BTC/USDT')
    assert result
    print(result)

def test_fetch_leverage_tiers():
    result = gains.fetch_leverage_tiers(symbols=['BTC/USDT'])
    assert result
    print(result)

def test_set_leverage():
    result = gains.set_leverage(leverage=100, symbol='BTC/USDT')
    assert result
    print(result)

def test_fetch_trades():
    result = gains.fetch_trades(symbol='BTC/USDT', since=1234567890, limit=100)
    assert result
    print(result)


if __name__ == "__main__":
    import ccxt
    gains = ccxt.gains({"apiKey": "apiKeyval", "secret": "secretval"})

    print(('=' * 100) + ' describe ' + ('=' * 100))
    test_describe()
    print(('=' * 100) + ' markets ' + ('=' * 100))
    test_fetch_markets()
    print(('=' * 100) + ' fetch_order ' + ('=' * 100))
    test_fetch_order()
    print(('=' * 100) + ' fetch_orders ' + ('=' * 100))
    test_fetch_orders()
    print(('=' * 100) + ' create_order ' + ('=' * 100))
    test_create_order()
    print(('=' * 100) + ' cancel_order ' + ('=' * 100))
    test_cancel_order()
    print(('=' * 100) + ' fetch_balance ' + ('=' * 100))
    test_fetch_balance()
    print(('=' * 100) + ' fetch_ohlcv ' + ('=' * 100))
    test_fetch_ohlcv()
    print(('=' * 100) + ' fetch_ticker ' + ('=' * 100))
    test_fetch_ticker()
    print(('=' * 100) + ' fetch_leverage_tiers ' + ('=' * 100))
    test_fetch_leverage_tiers()
    print(('=' * 100) + ' set_leverage ' + ('=' * 100))
    test_set_leverage()
    print(('=' * 100) + ' fetch_trades ' + ('=' * 100))
    test_fetch_trades()

