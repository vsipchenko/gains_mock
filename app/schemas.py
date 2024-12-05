from typing import List, Optional, Dict
from pydantic import BaseModel

class Order(BaseModel):
    id: str
    timestamp: int
    status: str
    symbol: str
    type: str
    timeInForce: Optional[str]
    side: str
    price: Optional[float]
    average: Optional[float]
    amount: float
    filled: float
    remaining: float
    cost: float
    trades: List[Dict]
    fee: Optional[Dict]


class OrderCreateRequest(BaseModel):
    pair: str               # "ETH/BTC"
    side: str               # "buy" or "sell"
    type: str               # "market" or "limit"
    amount: float           # Amount to trade in base currency
    price: Optional[float]  # Limit price in quote currency


class Balance(BaseModel):
    timestamp: int
    free: Dict[str, float]
    used: Dict[str, float]
    total: Dict[str, float]
    debt: Dict[str, float]

class Ticker(BaseModel):
    symbol: str
    timestamp: int
    high: float
    low: float
    bid: float
    bidVolume: Optional[float]
    ask: float
    askVolume: Optional[float]
    vwap: float
    open: float
    close: float
    previousClose: float
    baseVolume: float
    quoteVolume: float

class LeverageTier(BaseModel):
    tier: int
    notionalCurrency: str
    minNotional: float
    maxNotional: float
    maintenanceMarginRate: float
    maxLeverage: int


class Leverage(BaseModel):
    symbol: str
    longLeverage: int
    shortLeverage: int

class SetLeverageRequest(BaseModel):
    pair: str
    leverage: int
    long_leverage: Optional[int] = None
    short_leverage: Optional[int] = None

class Trade(BaseModel):
    id: str
    timestamp: int
    symbol: str
    order: str
    type: str
    side: str
    takerOrMaker: str
    price: float
    amount: float
    cost: float
    fee: Dict
    fees: List[Dict]


class Market(BaseModel):
    id: str
    symbol: str
    base: str
    baseId: str
    quote: str
    quoteId: str
    contract: Optional[bool] = True
    swap: Optional[bool] = True
