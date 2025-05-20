# app/models/friend.py
from app.models.db_model import DbModel
from config.db import session

from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Friend(DbModel):
    __tablename__ = 'friends'

    # Metodos de Db para Sqlalchemy
    user_id_1 = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_id_2 = Column(Integer, ForeignKey('users.id'), primary_key=True)
    favourite = Column(Boolean, default=False)
    blocked = Column(Boolean, default=False)

    # Relationships para Sqlalchemy
    user1 = relationship('User', foreign_keys=[user_id_1], back_populates='my_friends')
    user2 = relationship('User', foreign_keys=[user_id_2], back_populates='friend_of')

    def add_user_data(self):
        self.friend_name = self.user2.name
        self.friend_username = self.user2.username
        self.friend_profile_picture_url = self.user2.profile_picture_url

    @staticmethod
    def new_friendship(user_id, friend_id):
        if friend_id != user_id:  # No permitir agregar a uno mismo como amigo
            # Agrego una nueva entidad Friend para cada user 
            new_friend_1 = Friend(user_id_1=user_id, user_id_2=friend_id, favourite=False, blocked=False)
            new_friend_2 = Friend(user_id_1=friend_id, user_id_2=user_id, favourite=False, blocked=False)
            # Las guardo en db
            session.add(new_friend_1)
            session.add(new_friend_2)
            session.commit()

    @staticmethod
    def remove_friendship(user_id, friend_id):
        friend_relations = session.query(Friend).filter(
            # Busco Friend donde user o friend sea user_id_1 o user_id_2
            (Friend.user_id_1 == user_id) & (Friend.user_id_2 == friend_id) |
            (Friend.user_id_1 == friend_id) & (Friend.user_id_2 == user_id)
        ).all()

        # Borro todas las relaciones tanto del lado del user como el friend 
        for relation in friend_relations:
            session.delete(relation)

        session.commit()