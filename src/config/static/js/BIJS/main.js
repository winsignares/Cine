function addPelis() {
    // Obtener el título de la película
    const titulopelicula = event.target.closest('.movie-item').querySelector('.movie-item-title').textContent.trim();
  
    // Codificar el título de la película para incluirlo en la URL
    var url = '/fronted/indexDescripcion?movie=' + encodeURIComponent(titulopelicula);
    // Redirigir a la página indexAsientos con el título de la película en la URL
    window.location.href = url
  }
  
  function replaceLoginWithUsername() {
    const token = localStorage.getItem('token');

    if (token) {
        axios.get('/fronted/obtener_nombre_usuario', {
            params: {
                token: token
            }
        })
        .then(function(res) {
            const nombreUsuario = res.data.nombre_usuario;
            const userNameElement = document.getElementById('user-name');
            userNameElement.textContent = nombreUsuario;

            const userMenu = document.getElementById('user-menu');
            const userSubmenu = document.getElementById('user-submenu');
            userMenu.style.display = 'block';
            userMenu.addEventListener('click', function() {
                userSubmenu.classList.toggle('show');
            });

            const logoutLink = document.getElementById('logout');
            logoutLink.addEventListener('click', logout);
        })
        .catch(function(error) {
            console.log(error);
        });
    }
}

function logout() {
    localStorage.removeItem('token');
    window.location.href = 'http://127.0.0.1:5000/';
}

document.getElementById('user-menu').addEventListener('click', function() {
    const userSubmenu = document.getElementById('user-submenu');
    userSubmenu.classList.toggle('show');
});

replaceLoginWithUsername();
