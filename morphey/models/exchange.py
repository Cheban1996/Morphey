import ccxt.async_support as ccxt

from morphey.models.base import BaseDBMorphey


class Exchange(BaseDBMorphey):
    def __init__(self, api_key=None, api_secret=None):
        super().__init__()
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.collection = self.db['exchange']  # collection exchange
        self.exchange: ccxt.binance = getattr(ccxt, 'binance')()

    async def add_exchange(self):
        pass

    async def get_self(self, user_id):
        api_key, api_password = await self.collection.find_one(
            {'user_id': user_id}
        )
        return Exchange(api_key, api_password)

    async def get_markets(self):
        markets = await self.exchange.load_markets()
        symbols = self.exchange.symbols

        await self.exchange.close()
        markets = {symbol: market
                   for symbol, market in markets.items()
                   if 'USDT' in symbol}
        symbols = [symbol
                   for symbol in symbols
                   if 'USDT' in symbol]
        return markets, symbols
