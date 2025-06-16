var loggedUser = {};

document.addEventListener('DOMContentLoaded', function() {
    const userElement = document.getElementById("user-container");
    loggedUser = JSON.parse(userElement.dataset.user);
});

function updateProfile() {
    document.getElementById('profile-img').src = loggedUser.profile_picture_url;
    document.getElementById('user-name').innerText = loggedUser.name;
    document.getElementById('user-username').innerText = '('+loggedUser.username+')';
    document.getElementById('user-email').innerText = loggedUser.email;
}

function saveProfile() {
    const formData = {
        id: loggedUser.id,
        name: document.getElementById('name').value,
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        profile_picture_url: document.getElementById('profile_picture_url').value
    };

    fetch('/api/user/' + loggedUser.id + '/save-profile', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Perfil guardado:', data);
        loggedUser = Object.assign({}, loggedUser, data.user);
        updateProfile();
        alert('Perfil actualizado correctamente');
    })
    .catch(err => {
        console.error('Error al guardar perfil:', err);
        alert('Hubo un error al guardar el perfil');
    });
}