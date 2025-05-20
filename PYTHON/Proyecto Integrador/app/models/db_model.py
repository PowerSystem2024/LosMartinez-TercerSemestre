from config.db import session
from sqlalchemy.orm import declarative_base

# Declaro que la clase DbModel es una clase de sqlalchemy
Base = declarative_base()

class DbModel(Base):
    __abstract__ = True  # evita que SQLAlchemy cree una tabla para esta clase

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def toText(self):
        return self.__dict__

    @classmethod  # Metodo Estatico
    def all(cls):
        return session.query(cls).all()

    @classmethod  # Metodo Estatico
    def find(cls, pk):
        return session.get(cls, pk)

    def delete(self):
        session.delete(self)
        session.commit()

    def save(self):
        session.add(self)
        session.commit()
        session.refresh(self)