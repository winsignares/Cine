function sendNewPeliculas() {
  // Obtener los valores de los campos del formulario
  var id = document.getElementById('id').value;
  var titulo = document.getElementById('titulo').value;
  var genero = document.getElementById('genero').value;
  var duracion = document.getElementById('duracion').value;
  var sinopsis = document.getElementById('sinopsis').value;
  var director = document.getElementById('director').value;
  var imagen = document.getElementById('imagen').value;
  var video = document.getElementById('video').value
  
  // Crear un objeto con los datos de la película
  var pelicula = {
    id: id,
    titulo: titulo,
    genero: genero,
    duracion: duracion,
    sinopsis: sinopsis,
    director: director,
    imagen: imagen,
    video: video
  };
  
  // Realizar la solicitud POST al endpoint '/saveAdmin' en el servidor
  fetch('/fronted/saveAdmin', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(pelicula)
  })
  .then(response => {
    if (response.ok) {
      // La película se guardó exitosamente
      alert('La película se ha guardado correctamente');
    } else {
      // Ocurrió un error al guardar la película
      alert('Error al guardar la película');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}


function cargarDatosTabla() {
  axios.get('/fronted/mostrar_pelicula')
    .then(function(response) {
      var peliculas = response.data;
      var tableBody = document.getElementById('peliculas-lista');

      peliculas.forEach(function(pelicula) {
        var row = document.createElement('tr');

        var idCell = document.createElement('td');
        idCell.textContent = pelicula.ID;
        row.appendChild(idCell);

        var tituloCell = document.createElement('td');
        tituloCell.textContent = pelicula.Título;
        row.appendChild(tituloCell);

        var generoCell = document.createElement('td');
        generoCell.textContent = pelicula.Género;
        row.appendChild(generoCell);

        var duracionCell = document.createElement('td');
        duracionCell.textContent = pelicula.Duración;
        row.appendChild(duracionCell);

        var sinopsisCell = document.createElement('td');
        sinopsisCell.textContent = pelicula.Sinopsis;
        row.appendChild(sinopsisCell);

        var directorCell = document.createElement('td');
        directorCell.textContent = pelicula.Director;
        row.appendChild(directorCell);

        var imagenCell = document.createElement('td');
        imagenCell.textContent = pelicula['Img - link'];
        row.appendChild(imagenCell);

        var trailerCell = document.createElement('td');
        trailerCell.textContent = pelicula.trailer;
        row.appendChild(trailerCell);

        tableBody.appendChild(row);
      });
    })
    .catch(function(error) {
      console.log('Error al obtener los datos:', error);
    });
}
window.onload = function() {
  cargarDatosTabla();
};
