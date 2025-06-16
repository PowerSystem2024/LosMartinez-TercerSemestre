var loggedUser = {};
var friendsByGame = [];

document.addEventListener('DOMContentLoaded', function() {
    const userElement = document.getElementById("user-container");
    loggedUser = JSON.parse(userElement.dataset.user);
    friendsByGame = JSON.parse(userElement.dataset.friendsByGame);
    renderFriendsByGame(friendsByGame);
});

function renderFriendsByGame(friendsByGame) {
    friendsByGame.forEach(friendByGame => {
        const gameContainer = document.getElementById('game-friends-'+friendByGame.game_id);
            if(gameContainer) {
                gameContainer.innerHTML = null;
                friendByGame.friends.forEach(friend => {
                    const img = document.createElement('img');
                    img.className = 'profile-img';
                    img.src = friend.profile_picture_url;
                    gameContainer.appendChild(img);
                });
            }
    });
}
