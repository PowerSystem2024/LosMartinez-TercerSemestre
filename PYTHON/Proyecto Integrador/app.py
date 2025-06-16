from flask import Flask, render_template, request, jsonify
from app.services.users_service import UsersService
from app.services.friends_service import FriendsService
from app.services.games_service import GamesService

import sys
import os

app = Flask(__name__)

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# INDEX
@app.route('/api/user/<int:user_id>/store')
def store(user_id):
    user_object = UsersService.get_user_by_id(user_id)
    user = user_object.to_dict(['game_ids'])
    
    game_list = GamesService.get_all_games()
    games = [game.to_dict() for game in game_list]

    friends_by_game_list = GamesService.get_friends_by_game(user_id)

    return render_template('store.html', user=user, games=games, friends_by_game=friends_by_game_list)

# PERFIL
@app.route('/api/user/<int:user_id>/user_profile')
def user_profile(user_id):
    user_object = UsersService.get_user_by_id(user_id)
    user = user_object.to_dict(['friends'])
    print(user);

    return render_template('user_profile.html', user=user)

# BIBLIOTECA
@app.route('/api/user/<int:user_id>/library')
def games(user_id):
    user_object = UsersService.get_user_by_id(user_id)
    user = user_object.to_dict(['games'])

    friends_by_game_list = GamesService.get_friends_by_game(user_id)

    return render_template('library.html', user=user, friends_by_game=friends_by_game_list)


# COMPRAR JUEGO
@app.route('/api/user/<int:user_id>/add-game', methods=['POST'])
def add_game_to_user_route(user_id):
    data = request.get_json()
    game_id = data.get('game_id')

    try:
        new_user_game_object = GamesService.add_game_to_user(user_id, game_id)
        new_user_game = new_user_game_object.to_dict();
        return jsonify({'message': 'Juego agregado correctamente', 'user_game': new_user_game}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# EDITAR PERFIL
@app.route('/api/user/<int:user_id>/save-profile', methods=['POST'])
def update_user_profile_route(user_id):
    data = request.get_json()

    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    profile_picture_url = data.get('profile_picture_url')

    try:
        updated_user = UsersService.update_user(
            user_id,
            name=name,
            username=username,
            email=email,
            profile_picture_url=profile_picture_url
        )
        return jsonify({
            'message': 'Perfil actualizado correctamente',
            'user': updated_user.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)