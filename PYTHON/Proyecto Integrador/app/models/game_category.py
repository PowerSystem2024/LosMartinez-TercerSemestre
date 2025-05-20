# app/models/user.py
from app.models.db_model import DbModel

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class GameCategory(DbModel):
    __tablename__ = 'game_categories'

    game_id = Column(Integer, ForeignKey('games.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)

    game = relationship("Game", back_populates="game_categories")
    category = relationship("Category", back_populates="game_categories")