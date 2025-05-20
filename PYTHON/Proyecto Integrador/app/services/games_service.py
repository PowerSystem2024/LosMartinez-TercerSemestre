from app.models.user_game import UserGame
from app.models.user import User
from app.models.game import Game

class GamesService:

    @staticmethod
    def create_game(title, desc, release_date, price, is_owned, video_url, logo_img_url):
        game = Game(
            title=title,
            desc=desc,
            release_date=release_date,
            price=price,
            is_owned=is_owned,
            video_url=video_url,
            logo_img_url=logo_img_url
        )
        game.save()
        return game

    @staticmethod
    def update_game(game_id, title=None, desc=None, release_date=None, price=None, is_owned=None, video_url=None, logo_img_url=None):
        game = Game.find(game_id)

        game.title = title
        game.desc = desc
        game.release_date = release_date
        game.price = price
        game.is_owned = is_owned
        game.video_url = video_url
        game.logo_img_url = logo_img_url

        game.save()
        return game

    @staticmethod
    def delete_game(game_id):
        game = Game.find(game_id)
        game.delete()
        return True

    @staticmethod
    def get_game_by_id(game_id):
        return Game.find(game_id)

    @staticmethod
    def get_all_games():
        return Game.all()

    @staticmethod
    def add_game_to_user(user_id, game_id):
        user_game = UserGame(user_id=user_id, game_id=game_id)
        user_game.save()
        return user_game

    @staticmethod
    def remove_game_from_user(user_id, game_id):
        user_game = UserGame.query.filter_by(user_id=user_id, game_id=game_id).first()
        if user_game:
            user_game.delete()
            return True
        return False
    
    @staticmethod
    def get_friends_by_game(user_id):
        all_games_with_friends = Game.getByFriends(user_id)
        return list(all_games_with_friends)