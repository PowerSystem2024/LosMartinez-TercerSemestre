from flask import Flask, render_template
from app.services.users_service import UsersService
from app.services.friends_service import FriendsService
from app.services.games_service import GamesService

import sys
import os

app = Flask(__name__)

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)


@app.route('/')
def index():
    games = GamesService.get_all_games()
    friends_by_game = GamesService.get_friends_by_game(1)
    return render_template('index.html', games=games, friends_by_game=friends_by_game)

# @app.route('/user/<int:user_id>')
# def user_profile(user_id):
#     user = UsersService.get_user_by_id(user_id)
#     friends = UsersService.get_all_user_friends(user_id)
#     return render_template('user_profile.html')


if __name__ == '__main__':
    app.run(debug=True)