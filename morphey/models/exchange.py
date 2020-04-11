import ccxt.async_support as ccxt

from morphey.models.base import BaseDBMorphey


class Exchange(BaseDBMorphey):
    exchange: ccxt.binance

    def __init__(self,
                 user_id=None,
                 api_key=None,
                 api_secret=None):
        super().__init__()
        self.user_id = user_id
        self.__apiKey = api_key
        self.__apiSecret = api_secret
        self.collection = self.db['exchange']  # collection exchange
        if self.__apiKey and self.__apiSecret:
            self.exchange: ccxt.binance = getattr(ccxt, 'binance')({
                'apiKey': self.__apiKey,
                'secret': self.__apiSecret,
            })
        else:
            self.exchange: ccxt.binance = getattr(ccxt, 'binance')()


    async def add_exchange(self):
        pass

    async def get_self(self, user_id):
        api_key, api_password = await self.collection.find_one(
            {'user_id': user_id}
        )
        return Exchange(api_key, api_password)
