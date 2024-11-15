from typing import List, Optional, Dict

from starlette.requests import Request
from fastapi import APIRouter

from app.schemas import Order, Balance, Ticker, Leverage, Trade

api_router = APIRouter()


def get_hardcoded_order(**kwargs):
    order_data = {
        "id": "12345-67890",
        "timestamp": 1652376800000,
        "status": "open",
        "symbol": "BTC/USD",
        "type": "limit",
        "side": "buy",
        "price": 50000.0,
        "amount": 0.1,
        "filled": 0.0,
        "remaining": 0.1,
        "cost": 0.0,
        "timeInForce": None,
        "average": None,
        "trades": [],
        "fee": None
    }
    order_data.update(kwargs)
    return Order(**order_data)


@api_router.get("/orders", response_model=List[Order])
def fetch_orders(pair: Optional[str] = None, since: Optional[int] = None, limit: Optional[int] = None):
    return [get_hardcoded_order(id=f"{i}") for i in range(5)]


@api_router.get("/order", response_model=Order)
def fetch_order(request: Request, id: str, pair: Optional[str] = None):
    return get_hardcoded_order()

@api_router.post("/order", response_model=Order)
def create_order(order: Dict):
    return get_hardcoded_order(**order)


@api_router.delete("/order", response_model=Order)
def cancel_order(id: str, pair: Optional[str] = None):
    return get_hardcoded_order(status="canceled")


@api_router.get("/balance", response_model=Balance)
def fetch_balance():
    return Balance(
        timestamp=1652376800000,
        free={"BTC": 0.1, "USD": 5000.0},
        used={"BTC": 0.0, "USD": 0.0},
        total={"BTC": 0.1, "USD": 5000.0},
        debt={"BTC": 0.0, "USD": 0.0},
    )


@api_router.get("/ohlcv", response_model=List[List[float]])
def fetch_ohlcv(pair: str, timeframe: str, since: Optional[int] = None, limit: Optional[int] = None):
    return [
        [
            1504541580000,  # UTC timestamp in milliseconds, integer
            4235.4,  # (O)pen price, float
            4240.6,  # (H)ighest price, float
            4230.0,  # (L)owest price, float
            4230.7,  # (C)losing price, float
            37.72941911  # (V)olume float in base currency
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


@api_router.get("/ticker", response_model=Ticker)
def fetch_ticker(pair: str):
    return Ticker(
        symbol="BTC/USD",
        timestamp=1652376800000,
        high=50000.0,
        low=49000.0,
        bid=49500.0,
        bidVolume=0.1,
        ask=50500.0,
        askVolume=0.1,
        vwap=50000.0,
        open=49000.0,
        close=50000.0,
        previousClose=49000.0,
        baseVolume=0.1,
        quoteVolume=5000.0,
    )


@api_router.get("/leverage_tiers", response_model=Dict[str, list])
def fetch_leverage_tiers():
    return {
        "BTC/USD": [
            {
                "tier": 1,
                "notionalCurrency": "USD",
                "minNotional": 10.0,
                "maxNotional": 100.0,
                "maintenanceMarginRate": 0.01,
                "maxLeverage": 10
            },
            {
                "tier": 2,
                "notionalCurrency": "USD",
                "minNotional": 100.0,
                "maxNotional": 1000.0,
                "maintenanceMarginRate": 0.02,
                "maxLeverage": 20
            }
        ]
    }



@api_router.post("/leverage", response_model=Leverage)
def set_leverage(leverage: Dict):
    return Leverage(symbol="BTC/USD", longLeverage=100, shortLeverage=75)


@api_router.get("/trades", response_model=List[Trade])
def fetch_trades(symbol: Optional[str] = None, order_id: Optional[str] = None, since: Optional[int] = None, limit: Optional[int] = None):
    return [
        Trade(
            id="12345-67890",
            timestamp=1652376800000,
            symbol="BTC/USD",
            order="12345-67890",
            type="limit",
            side="buy",
            takerOrMaker="taker",
            price=50000.0,
            amount=0.1,
            cost=5000.0,
            fee=[
                {
                    "cost": 0.0015,
                    "currency": "ETH",
                    "rate": 0.002
                }
            ]
        ),
        Trade(
            id="12345-67891",
            timestamp=1652376801000,
            symbol="BTC/USD",
            order="12345-67891",
            type="limit",
            side="sell",
            takerOrMaker="maker",
            price=50000.0,
            amount=0.1,
            cost=5000.0,
            fee=[
                {
                    "cost": 0.0015,
                    "currency": "ETH",
                    "rate": 0.002
                }
            ]
        )
    ]
