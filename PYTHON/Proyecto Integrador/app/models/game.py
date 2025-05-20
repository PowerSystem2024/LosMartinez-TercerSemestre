# app/models/game.py
from app.models.db_model import DbModel
from app.models.user import User
from app.models.user_game import UserGame
from app.models.friend import Friend
from app.models.category import Category
from app.models.game_category import GameCategory

from config.db import session
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from collections import defaultdict

class Game(DbModel):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    desc = Column(String)   
    release_date = Column(String)
    price = Column(Float)
    video_url = Column(String)
    logo_img_url = Column(String)

    game_categories = relationship("GameCategory", back_populates="game")
    user_games = relationship("UserGame", back_populates="game")

    @property
    def categories(self):
        return [gc.category for gc in self.game_categories]

    @property
    def users(self):
        return [gu.user for gu in self.user_games]

    def __init__(self, title, desc=None, release_date=None, price=None,
                 video_url=None, logo_img_url=None):
        self.title = title
        self.desc = desc
        self.release_date = release_date
        self.price = price
        self.video_url = video_url
        self.logo_img_url = logo_img_url

    def getByFriends(user_id):
        all_games_by_friends = (
            session.query(
                UserGame.game_id,
                User.id.label("user_id"),
                User.profile_picture_url
            )
            .join(Friend, User.id == Friend.user_id_2)
            .join(UserGame, UserGame.user_id == Friend.user_id_2)
            .filter(
                User.id != user_id,
                Friend.user_id_1 == user_id
            )
            .order_by(UserGame.game_id)
            .all()
        )
        
        games_dictionary = defaultdict(list)
        for row in all_games_by_friends:
            friend_data = {
                "friend_id": row.user_id,
                "profile_picture_url": row.profile_picture_url
            }
            games_dictionary[row.game_id].append(friend_data)

        return [
            {
                "game_id": game_id,
                "friends": friends
            }
            for game_id, friends in games_dictionary.items()
        ]
