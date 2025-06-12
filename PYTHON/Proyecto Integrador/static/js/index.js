const userElement = document.getElementById("user-container");
const loggedUser = JSON.parse(userElement.dataset.user);
console.log(loggedUser);
var gamesById = {};

document.querySelectorAll(".game-info").forEach(div => {
    const game = JSON.parse(div.dataset.game);
    gamesById[game.id] = game;

    div.addEventListener('click', function(event) {
        console.log(game);
        setGameAsFeatured(game);
    });
});

function setGameAsFeatured(game) {
    document.getElementById('fg-title').innerHTML = game.title;
    document.getElementById('fg-image').src = game.logo_img_url;
    document.getElementById('fg-description').innerHTML = game.desc;
    document.getElementById('fg-relaese').innerHTML = game.release_date;
    document.getElementById('fg-price').innerHTML = game.price;
    
    document.getElementById('fg-video-src').src = game.video_url;
    document.getElementById('fg-video').load();

    // document.getElementById('fg-tags').innerHTML = game.;
}

function buyGame(game) {
    fetch('/api/user/123/add-game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ game_id: 456 })
    })
    .then(res => res.json())
    .then(data => {
        console.log('Respuesta:', data);
    })
    .catch(err => {
        console.error('Error:', err);
    });
}