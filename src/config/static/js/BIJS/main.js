const { default: axios } = require("axios");

function addPelis() {
    // Obtener el título de la película
    const titulopelicula = event.target.closest('.movie-item').querySelector('.movie-item-title').textContent.trim();
  
    // Codificar el título de la película para incluirlo en la URL
    var url = '/fronted/indexDescripcion?movie=' + encodeURIComponent(titulopelicula);
    // Redirigir a la página indexAsientos con el título de la película en la URL
    window.location.href = url
  }
  
function showNameUser() {
  itemValues = sessionStorage.getItem('token',  token)
  axios.get('/fronted/nameUser', {
    'item':itemValues
  })
  .then(function(res){ 
    const user = res.data.nameUser
    const newNameUser = document.getElementById("Update-nameUser")
    newNameUser.innerHTML = `
    <span id="Update-nameUser" class="user-name" onclick="toggleDropdown()">${user}</span>
    `
  })
  .catch((err) => {
    console.log(err);
  })
}

sessionStorage.setItem('token', token);

window.onload = showNameUser()