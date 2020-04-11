from morphey.models.base import BaseDBMorphey
from morphey.schemas.user import SchemaUser
import marshmallow
from pymongo.errors import PyMongoError


class User(BaseDBMorphey):

    def __init__(self):
        super().__init__()
        self.collection = self.db['users']

    async def create_user(self, data: dict):
        try:
            x = await self.collection.insert_one(data)
            print(x.inserted_id)
            return 'ok'
        except PyMongoError as e:
            # TODO need log
            print(e)
            return {'error': 'Please repeat later'}
        except BaseException as e:
            # TODO need log
            print(e)
            return {'error': 'Please repeat later'}

    @staticmethod
    async def get_users():
        return [SchemaUser().dump(item)
                async for item in User().collection.find()]
