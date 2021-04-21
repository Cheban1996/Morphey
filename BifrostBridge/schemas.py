from pydantic import BaseModel


class DataKlineSchema(BaseModel):
    t: int  # 123400000, // Kline start time
    T: int  # 123460000, // Kline close time
    s: str  # "BNBBTC",  // Symbol
    i: str  # "1m",      // Interval
    f: int  # 100,       // First trade ID
    L: int  # 200,       // Last trade ID
    o: float  # "0.0010",  // Open price
    c: float  # "0.0020",  // Close price
    h: float  # 0.0025",  // High price
    l: float  # "0.0015",  // Low price
    v: float  # "1000 ",    // Base asset volume
    n: int  # 100,       // Number of trades
    x: bool  # false,     // Is this kline closed?
    q: float  # "1.0000",  // Quote asset volume
    V: float  # "500",     // Taker buy base asset volume
    Q: float  # "0.500",   // Taker buy quote asset volume
    B: int  # "123456"   // Ignore


class StreamKlineSchema(BaseModel):
    e: str  # "kline",     // Event type
    E: int  # 123456789,   // Event time
    s: str  # "BNBBTC",    // Symbol
    k: DataKlineSchema  # Data Kline
