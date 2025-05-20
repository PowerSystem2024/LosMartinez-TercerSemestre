# app/services/users_service.py
from app.models.friend import Friend

class FriendsService:
    
    @staticmethod
    def create_friend(user_id, friend_id):
        friend = Friend.new_friendship(user_id, friend_id)
        return friend
    
    @staticmethod
    def remove_friend(user_id, friend_id):
        Friend.remove_friendship(user_id, friend_id)
        return True