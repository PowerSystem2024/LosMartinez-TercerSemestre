# app/models/user.py
from app.models.db_model import DbModel

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class UserGame(DbModel):
    __tablename__ = 'user_games'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'), primary_key=True)

    game = relationship("Game", back_populates="user_games")
    user = relationship("User", back_populates="user_games")