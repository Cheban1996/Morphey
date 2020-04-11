from ccxt import async_support as ccxt
from morphey.models.exchange import Exchange


class ServiceExchange(Exchange):
    # Private
    async def fetch_balance(self):
        pass

    async def create_order(self):
        pass

    async def cancel_order(self):
        pass

    async def fetch_order(self):
        pass

    async def fetch_open_order(self):
        pass

    async def fetch_closed_orders(self):
        pass

    # Public

    async def fetch_markets(self):
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

    async def fetch_ohlcv(self):
        pass
