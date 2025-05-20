# app/services/users_service.py

from app.models.user import User

class UsersService:

    @staticmethod
    def create_user(name, username, password, email, profile_picture_url):
        user = User(
            name=name, 
            username=username, 
            password=password, 
            email=email,
            profile_picture_url=profile_picture_url
        )
        user.save()
        return user

    @staticmethod
    def update_user(user_id, name=None, username=None, password=None, email=None, profile_picture_url=None):
        user = User.find(user_id)

        user.name = name
        user.username = username
        user.password = password
        user.email = email
        user.profile_picture_url = profile_picture_url

        user.save()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.find(user_id)
        user.delete()
        return True

    @staticmethod
    def get_user_by_id(user_id):
        return User.find(user_id)

    @staticmethod
    def get_all_users():
        return User.all()

    @staticmethod
    def get_user_friends(user_id):
        user = User.find(user_id)
        return user.notBlockedFriends()

    @staticmethod
    def get_all_user_friends(user_id):
        user = User.find(user_id)
        return user.allFriends()
    
    @staticmethod
    def get_user_games(user_id):
        user = User.find(user_id)
        return user.allGames()
