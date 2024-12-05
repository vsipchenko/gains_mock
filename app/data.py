from typing import List

from app.schemas import Order, Market, Balance, Ticker, LeverageTier, Leverage, Trade


def get_order(**kwargs) -> Order:
    data = {
        'id': '12345-67890',
        'timestamp': 1652376800000,
        'status': 'open',
        'symbol': 'BTC/USDT',
        'type': 'limit',
        'side': 'buy',
        'price': 50000.0,
        'amount': 0.1,
        'filled': 0.0,
        'remaining': 0.1,
        'cost': 0.0,
        'timeInForce': None,
        'average': None,
        'trades': [],
        'fee': {
            'currency': 'BTC',
            'cost': 0.0009,
            'rate': 0.002,

        }
    }
    data.update(kwargs)
    return Order(**data)


def get_market(**kwargs) -> Market:
    data = {
        'id': 'BTC/USDT',
        'symbol': 'BTC/USDT',
        'base': 'BTC',
        'quote': 'USDT',
        'baseId': 'btc',
        'quoteId': 'usdt',
        'contract': True,
        'swap': True,
    }
    data.update(kwargs)
    return Market(**data)

def get_balance(**kwargs) -> Balance:
    data = {
        'timestamp': 1652376800000,
        'free': {'BTC': 0.1, 'USD': 5000.0},
        'used': {'BTC': 0.0, 'USD': 0.0},
        'total': {'BTC': 0.1, 'USD': 5000.0},
        'debt': {'BTC': 0.0, 'USD': 0.0},
    }
    data.update(kwargs)
    return Balance(**data)

def get_ohlcv() -> List[List[float]]:
    return [
        [
            1504541580000,  # UTC timestamp in milliseconds, integer
            4235.4,         # (O)pen price, float
            4240.6,         # (H)ighest price, float
            4230.0,         # (L)owest price, float
            4230.7,         # (C)losing price, float
            37.72941911     # (V)olume float in base currency
        ],
        [
            1504541640000,
            4231.6,
            4240.7,
            4231.6,
            4236.2,
            61.46897393
        ]
    ]

def get_ticker(**kwargs) -> Ticker:
    data = {
        'symbol': 'BTC/USDT',
        'timestamp': 1652376800000,
        'high': 50000.0,
        'low': 49000.0,
        'bid': 49500.0,
        'bidVolume': None,
        'ask': 49550.0,
        'askVolume': None,
        'vwap': 49525.0,
        'open': 49500.0,
        'close': 49550.0,
        'previousClose': 49500.0,
        'baseVolume': 100.0,
        'quoteVolume': 5000000.0,
    }
    data.update(kwargs)
    return Ticker(**data)

def get_leverage_tier(**kwargs) -> LeverageTier:
    data = {
        'tier': 1,
        'notionalCurrency': 'USD',
        'minNotional': 10.0,
        'maxNotional': 100.0,
        'maintenanceMarginRate': 0.01,
        'maxLeverage': 10
    }
    data.update(kwargs)
    return LeverageTier(**data)

def get_leverage(**kwargs) -> Leverage:
    data = {
        'symbol': 'BTC/USDT',
        'longLeverage': 100,
        'shortLeverage': 75
    }
    kwargs["symbol"] = kwargs.pop('pair', None)
    data.update(kwargs)
    return Leverage(**data)

def get_trade(**kwargs) -> Trade:
    data = {
        'id': '12345-67890',
        'timestamp': 1652376800000,
        'symbol': 'BTC/USDT',
        'order': '12345-67890',
        'type': 'limit',
        'side': 'buy',
        'takerOrMaker': 'taker',
        'price': 50000.0,
        'amount': 0.1,
        'cost': 5000.0,
        'fee': {
            'cost': 0.0015,
            'currency': 'ETH',
            'rate': 0.002
        },
        'fees': [
            {
                'cost': 0.0015,
                'currency': 'ETH',
                'rate': 0.002
            }
        ]
    }
    data.update(kwargs)
    return Trade(**data)
