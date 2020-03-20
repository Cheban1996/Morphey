import motor.motor_asyncio as motor


class BaseDBMorphey:
    def __init__(self):
        self.client = motor.AsyncIOMotorClient()
        self.db = self.client['morphey']
