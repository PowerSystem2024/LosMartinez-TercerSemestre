# app/models/user.py
from app.models.db_model import DbModel

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Category(DbModel):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    tag = Column(String, nullable=False)

    game_categories = relationship("GameCategory", back_populates="category")

    @property
    def games(self):
        return [gc.game for gc in self.game_categories]