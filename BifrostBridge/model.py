import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection, InsertOneResult


class BaseModel:
    def __init__(self, database, collection):
        self.client = AsyncIOMotorClient()
        self.database = self.client[database]
        self.collection: Collection = self.database[collection]

    async def get_one(self):
        raise NotImplemented

    async def get_many(self):
        raise NotImplemented

    async def create(self, document: dict):
        result: InsertOneResult = await self.collection.insert_one(document)
        return result.inserted_id

    async def update(self):
        raise NotImplemented

    async def delete(self):
        raise NotImplemented


class BifrostBridgeModel(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, database='bifrost_bridge', collection='klines')


bifrost_bridge = BifrostBridgeModel()
