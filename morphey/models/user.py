from morphey.models.base import BaseDBMorphey
from morphey.schemas.user import SchemaUser
import marshmallow


class User(BaseDBMorphey):

    def __init__(self):
        super().__init__()
        self.collection = self.db['users']

    async def create_user(self, **kwargs):
        try:
            await self.collection.insert_one(SchemaUser().load(kwargs))
            return 'ok'
        except marshmallow.exceptions.ValidationError as e:
            return e.normalized_messages()

    @staticmethod
    async def get_users():
        return [SchemaUser().dump(item)
                async for item in User().collection.find()]
