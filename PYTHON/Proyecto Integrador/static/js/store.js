var gamesById = {};
var featuredGameId = null;
var loggedUser = {};
var friendsByGame = [];

document.addEventListener('DOMContentLoaded', function() {
    const userElement = document.getElementById("user-container");
    loggedUser = JSON.parse(userElement.dataset.user);
    friendsByGame = JSON.parse(userElement.dataset.friendsByGame);

    document.querySelectorAll(".game-info").forEach(div => {
        const game = JSON.parse(div.dataset.game);
        gamesById[game.id] = game;

        div.addEventListener('click', function(event) {
            setGameAsFeatured(game);
        });
    });
    
    featuredGameId = Object.keys(gamesById)[0]; 
    setGameAsFeatured(gamesById[featuredGameId]);
});

function setGameAsFeatured(game) {
    featuredGameId = game.id;

    document.getElementById('fg-title').innerHTML = game.title;
    document.getElementById('fg-image').src = game.logo_img_url;
    document.getElementById('fg-description').innerHTML = game.desc;
    document.getElementById('fg-relaese').innerHTML = game.release_date;
    document.getElementById('fg-price').innerHTML = '$' + game.price;
    document.getElementById('fg-video-src').src = game.video_url;
    document.getElementById('fg-video').load();

    setBuyButtonStatus(game.id);
    
    const tagsContainer = document.getElementById('fg-tags');
    tagsContainer.innerHTML = null;

    game.categories.forEach(category => {
        const tag = document.createElement('div');
        tag.classList.add('tag', 'simple-button');
        tag.textContent = category.tag.toUpperCase();
        tagsContainer.appendChild(tag);
    })
        
    const friendsContainer = document.getElementById('fg-friends');
    const friendByGame = friendsByGame.find(fbg => fbg.game_id == featuredGameId);
    
    friendsContainer.innerHTML = null;
    if(friendByGame) {
        friendByGame.friends.forEach(friend => {
            const img = document.createElement('img');
            img.className = 'small-profile-img';
            img.src = friend.profile_picture_url;
            friendsContainer.appendChild(img);
        });
    }
}

function hasGameBought(game_id) {
    return loggedUser.game_ids.includes(game_id);
}

function setBuyButtonStatus(game_id) {
    const buyButton = document.getElementById('buy-button')
    
    if(hasGameBought(game_id)) {
        buyButton.innerText = "EN BIBLIOTECA";
        buyButton.onclick = null;
        buyButton.classList.add('disabled');
    } else {
        buyButton.innerText = "COMPRAR";
        buyButton.onclick = buyGame;
        buyButton.classList.remove('disabled');
    }
}

function buyGame() {
    fetch('/api/user/'+loggedUser.id+'/add-game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ game_id: featuredGameId })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response:', data);
        const game_id = data.user_game.game.id;
        loggedUser.game_ids.push(game_id);
        setBuyButtonStatus(game_id);
        alert('El juego fue agregado a tu biblioteca!');
    })
    .catch(err => {
        console.error('Error:', err);
    });
}