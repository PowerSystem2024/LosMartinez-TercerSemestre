# app/models/user.py
from app.models.db_model import DbModel
from app.models.friend import Friend
from config.db import session

from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import relationship, aliased

class User(DbModel):
    __tablename__ = 'users'

    # Metodos de Db para Sqlalchemy
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    username = Column(String(100))
    password = Column(String(100))
    email = Column(String(100))
    profile_picture_url = Column(String(255))

    # Relationships para Sqlalchemy
    my_friends = relationship('Friend', foreign_keys='Friend.user_id_1', back_populates='user1')
    friend_of = relationship('Friend', foreign_keys='Friend.user_id_1', back_populates='user2')
    user_games = relationship("UserGame", back_populates="user")

    @property
    def games(self):
        return [gu.game for gu in self.user_games]

    def __init__(self, id=None, name=None, username=None, password=None, email=None, profile_picture_url=None):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.profile_picture_url = profile_picture_url

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'profile_picture_url': self.profile_picture_url
        }

    def allFriends(self):
        # Creo una query generica con Friends
        query = User.getFriendsQuery(self)
        result = query.fetchall()

        # Procesar los resultados
        return User.formatFriendData(result)

    def notBlockedFriends(self):
        # Creo una query generica con Friends
        query = User.getFriendsQuery(self)
        query.filter(Friend.blocked == False)  # Filtrar por no bloqueados
        query.order_by(Friend.favourite.desc())  # Ordenar por favorito, descendente
        result = query.fetchall()

        # Procesar los resultados
        return User.formatFriendData(result)
    
    def allGames(self):
        return [ug.game for ug in self.user_games]
    
    @staticmethod
    def getFriendsQuery(self):
        my_friend = aliased(User)

        return session.execute(
            select(
                Friend.favourite,
                Friend.blocked,
                Friend.user_id_2.label('friend_id'),
                my_friend.name.label('friend_name'),
                my_friend.username,
                my_friend.profile_picture_url
            )
            .join(my_friend, my_friend.id == Friend.user_id_2)
            .filter(Friend.user_id_1 == self.id)
        )

    @staticmethod
    def formatFriendData(result):
        print(f"{result}")
        return [
            {
                'favourite': row[0],
                'blocked': row[1],
                'friend_user': User(
                    id=row[2], 
                    name=row[3], 
                    username=row[4], 
                    password=None, 
                    email=None,
                    profile_picture_url=row[5]
                )
            }
            for row in result
        ]