from typing import List, Optional, Dict

from starlette.requests import Request
from fastapi import APIRouter

from app.data import get_market, get_order, get_balance, get_ohlcv, get_ticker, get_leverage_tier, get_leverage, \
    get_trade
from app.schemas import Order, Balance, Ticker, Leverage, Trade, OrderCreateRequest, SetLeverageRequest, LeverageTier, \
    Market

api_router = APIRouter()


@api_router.get('/markets', response_model=List[Market])
def fetch_markets():
    # [
    #     {
    #         'id': 'BTC/USDT',
    #         'symbol': 'BTC/USDT',
    #         'base': 'BTC',
    #         'quote': 'USDT',
    #         'baseId': 'btc',
    #         'quoteId': 'usdt',
    #         'contract': True,
    #         'type': 'swap',
    #     },
    #     {
    #         'id': 'ETH/USDT',
    #         'symbol': 'ETH/USDT',
    #         'base': 'ETH',
    #         'quote': 'USDT',
    #         'baseId': 'eth',
    #         'quoteId': 'usdt',
    #         'contract': True,
    #         'type': 'swap',
    #     },
    # ]
    return [get_market() for _ in range(5)]

@api_router.get('/orders', response_model=List[Order])
def fetch_orders(pair: Optional[str] = None, since: Optional[int] = None, limit: Optional[int] = None):
    # [
    #     {
    #         'id': '12345-67890',
    #         'timestamp': 1652376800000,
    #         'status': 'open',
    #         'symbol': 'BTC/USDT',
    #         'type': 'limit',
    #         'side': 'buy',
    #         'price': 50000.0,
    #         'amount': 0.1,
    #         'filled': 0.0,
    #         'remaining': 0.1,
    #         'cost': 0.0,
    #         'timeInForce': None,
    #         'average': None,
    #         'trades': [],
    #         'fee': {
    #             'currency': 'BTC',
    #             'cost': 0.0009,
    #             'rate': 0.002,
    # 
    #         }
    #     },
    #     {
    #         'id': '12345-67891',
    #         'timestamp': 1652376800000,
    #         'status': 'open',
    #         'symbol': 'BTC/USDT',
    #         'type': 'limit',
    #         'side': 'buy',
    #         'price': 50000.0,
    #         'amount': 0.1,
    #         'filled': 0.0,
    #         'remaining': 0.1,
    #         'cost': 0.0,
    #         'timeInForce': None,
    #         'average': None,
    #         'trades': [],
    #         'fee': {
    #             'currency': 'BTC',
    #             'cost': 0.0009,
    #             'rate': 0.002,
    # 
    #         }
    #     },
    # ]
    return [get_order(id=f'order_id_{i}') for i in range(5)]


@api_router.get('/order', response_model=Order)
def fetch_order(request: Request, id: str, pair: Optional[str] = None):
    # {
    #     'id': '12345-67890',
    #     'timestamp': 1652376800000,
    #     'status': 'open',
    #     'symbol': 'BTC/USDT',
    #     'type': 'limit',
    #     'side': 'buy',
    #     'price': 50000.0,
    #     'amount': 0.1,
    #     'filled': 0.0,
    #     'remaining': 0.1,
    #     'cost': 0.0,
    #     'timeInForce': None,
    #     'average': None,
    #     'trades': [],
    #     'fee': {
    #         'currency': 'BTC',
    #         'cost': 0.0009,
    #         'rate': 0.002,
    # 
    #     }
    # }
    return get_order()

@api_router.post('/order', response_model=Order)
def create_order(payload: OrderCreateRequest):
    # {
    #     'id': '12345-67890',
    #     'timestamp': 1652376800000,
    #     'status': 'open',
    #     'symbol': 'BTC/USDT',
    #     'type': 'limit',
    #     'side': 'buy',
    #     'price': 50000.0,
    #     'amount': 0.1,
    #     'filled': 0.0,
    #     'remaining': 0.1,
    #     'cost': 0.0,
    #     'timeInForce': None,
    #     'average': None,
    #     'trades': [],
    #     'fee': {
    #         'currency': 'BTC',
    #         'cost': 0.0009,
    #         'rate': 0.002,
    # 
    #     }
    # }
    return get_order(**payload.dict())


@api_router.delete('/order', response_model=Order)
def cancel_order(id: str, pair: Optional[str] = None):
    # {
    #     'id': '12345-67890',
    #     'timestamp': 1652376800000,
    #     'status': 'cancelled',
    #     'symbol': 'BTC/USDT',
    #     'type': 'limit',
    #     'side': 'buy',
    #     'price': 50000.0,
    #     'amount': 0.1,
    #     'filled': 0.0,
    #     'remaining': 0.1,
    #     'cost': 0.0,
    #     'timeInForce': None,
    #     'average': None,
    #     'trades': [],
    #     'fee': {
    #         'currency': 'BTC',
    #         'cost': 0.0009,
    #         'rate': 0.002,
    # 
    #     }
    # }
    return get_order(status='cancelled')


@api_router.get('/balance', response_model=Balance)
def fetch_balance():
    # {
    #     'timestamp': 1652376800000,
    #     'free': {'BTC': 0.1, 'USD': 5000.0},
    #     'used': {'BTC': 0.0, 'USD': 0.0},
    #     'total': {'BTC': 0.1, 'USD': 5000.0},
    #     'debt': {'BTC': 0.0, 'USD': 0.0},
    # }
    return get_balance()


@api_router.get('/ohlcv', response_model=List[List[float]])
def fetch_ohlcv(pair: str, timeframe: str, since: Optional[int] = None, limit: Optional[int] = None):
    # [
    #     [
    #         1504541580000,  # UTC timestamp in milliseconds, integer
    #         4235.4,         # (O)pen price, float
    #         4240.6,         # (H)ighest price, float
    #         4230.0,         # (L)owest price, float
    #         4230.7,         # (C)losing price, float
    #         37.72941911     # (V)olume float in base currency
    #     ],
    #     [
    #         1504541640000,
    #         4231.6,
    #         4240.7,
    #         4231.6,
    #         4236.2,
    #         61.46897393
    #     ]
    # ]
    return get_ohlcv()


@api_router.get('/ticker', response_model=Ticker)
def fetch_ticker(pair: str):
    # {
    #     'symbol': 'BTC/USDT',
    #     'timestamp': 1652376800000,
    #     'high': 50000.0,
    #     'low': 49000.0,
    #     'bid': 49500.0,
    #     'bidVolume': None,
    #     'ask': 49550.0,
    #     'askVolume': None,
    #     'vwap': 49525.0,
    #     'open': 49500.0,
    #     'close': 49550.0,
    #     'previousClose': 49500.0,
    #     'baseVolume': 100.0,
    #     'quoteVolume': 5000000.0,
    # }
    return get_ticker()


@api_router.get('/leverage_tiers', response_model=Dict[str, List[LeverageTier]])
def fetch_leverage_tiers():
    # [
    #     {
    #         'tier': 1,
    #         'notionalCurrency': 'USD',
    #         'minNotional': 10.0,
    #         'maxNotional': 100.0,
    #         'maintenanceMarginRate': 0.01,
    #         'maxLeverage': 10
    #     },
    #     {
    #         'tier': 2,
    #         'notionalCurrency': 'USD',
    #         'minNotional': 100.0,
    #         'maxNotional': 1000.0,
    #         'maintenanceMarginRate': 0.01,
    #         'maxLeverage': 10
    #     },
    # ]
    return {'BTC/USDT': [get_leverage_tier(tier=i) for i in range(5)]}



@api_router.post('/leverage', response_model=Leverage)
def set_leverage(payload: SetLeverageRequest):
    # {
    #     'symbol': 'BTC/USDT',
    #     'longLeverage': 100,
    #     'shortLeverage': 75
    # }
    return get_leverage(**payload.dict())


@api_router.get('/trades', response_model=List[Trade])
def fetch_trades(symbol: Optional[str] = None, order_id: Optional[str] = None, since: Optional[int] = None, limit: Optional[int] = None):
    # {
    #     'id': '12345-67890',
    #     'timestamp': 1652376800000,
    #     'symbol': 'BTC/USDT',
    #     'order': '12345-67890',
    #     'type': 'limit',
    #     'side': 'buy',
    #     'takerOrMaker': 'taker',
    #     'price': 50000.0,
    #     'amount': 0.1,
    #     'cost': 5000.0,
    #     'fee': {
    #         'cost': 0.0015,
    #         'currency': 'ETH',
    #         'rate': 0.002
    #     },
    #     'fees': [
    #         {
    #             'cost': 0.0015,
    #             'currency': 'ETH',
    #             'rate': 0.002
    #         }
    # ]
    return [get_trade(id=f'trade_id_{i}') for i in range(5)]

