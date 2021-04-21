import os
from typing import List

import aioredis


class RedisStore:
    redis: aioredis

    async def setup(self):
        host = os.getenv('REDIS_URL', '127.0.0.1')
        port = os.getenv('REDIS_PORT', '6379')
        self.redis = await aioredis.create_redis_pool(f"redis://{host}:{port}")
        await self.setup_data()

    async def get_symbols(self) -> List[str]:
        template = "wss://stream.binance.com/stream?streams={0}@kline_{1}"
        urls = await self.redis.hgetall('active_symbols')
        return [template.format(symbol.decode(), candle_size.decode()) for symbol, candle_size in urls.items()]

    async def update_price_ticker(self, symbol: str, data: str):
        await self.redis.hset('KLINE', symbol, data)

    async def setup_data(self):
        self.redis.hset('active_symbols', 'btcusdt', '1m')

    async def close(self):
        self.redis.close()
        await self.redis.wait_closed()
