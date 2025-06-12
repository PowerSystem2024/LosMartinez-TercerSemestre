from flask import Flask, render_template, request
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
    user_object = UsersService.get_user_by_id(1)
    user = user_object.to_dict()
    
    game_objects = GamesService.get_all_games()
    games = [game.to_dict() for game in game_objects]
    
    friends_by_game = GamesService.get_friends_by_game(1)
    # sacar print
    print(friends_by_game)
    
    return render_template('index.html', user=user, games=games, friends_by_game=friends_by_game)


@app.route('/api/user/<int:user_id>/add-game', methods=['POST'])
def add_game_to_user_route(user_id):
    data = request.get_json()
    game_id = data.get('game_id')

    try:
        user_game = GamesService.add_game_to_user(user_id, game_id)
        return jsonify({'message': 'Juego agregado correctamente', 'user_game_id': user_game.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @app.route('/user/<int:user_id>')
# def user_profile(user_id):
#     user = UsersService.get_user_by_id(user_id)
#     friends = UsersService.get_all_user_friends(user_id)
#     return render_template('user_profile.html')


if __name__ == '__main__':
    app.run(debug=True)