from sqlalchemy import String, Integer, Column

from morphey.models import Base


class User(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(length=50), nullable=False, default='')
    last_name = Column(String(length=50), nullable=False, default='')
    password = Column(String(length=1048), nullable=False)
    email_name = Column(String(length=126), nullable=False)

    async def get_by_id(self, id):
        pass
