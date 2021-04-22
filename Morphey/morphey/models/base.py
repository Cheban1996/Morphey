import os
from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import update, delete
import databases

POSTGRES_USER = os.getenv('POSTGRES_USER', 'morphey_db')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'morphey_db')
POSTGRES_SERVER = os.getenv('POSTGRES_SERVER', 'morphey_db')
POSTGRES_DB = os.getenv('POSTGRES_DB', '127.0.0.1:54321')
url = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"


morphey_db = databases.Database(url)


@as_declarative()
class Base:
    id: Any
    __name__: str

    def __init__(self, db=morphey_db):
        self.db = db

    @declared_attr
    def __tablename__(cls) -> str:
        name = "".join([symbol if symbol.islower() else f" {symbol}" for symbol in cls.__name__])
        name = name.strip()
        name = name.replace(' ', '_')
        return name.lower()

    async def get_by_id(cls, id):
        query = update(cls.__class__).where(cls.__table__.c.id == cls.id).values(**kwargs)
        return await cls.db.execute(query)

    async def update(cls, **kwargs):
        query = update(cls.__class__).where(cls.__table__.c.id == cls.id).values(**kwargs)
        await cls.db.execute(query)

    async def delete(cls):
        query = delete(cls.__class__).where(cls.__table__.c.id == cls.id)
        await cls.db.execute(query)

    def dict(cls) -> dict:
        fields = [key for key, value in cls.__class__.__dict__.items() if hasattr(value, 'default')]
        return {item: getattr(cls, item, None) for item in fields}
