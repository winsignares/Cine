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


window.onload = function() {
  cargarDatosTabla();
};

function cargarDatosTabla() {
  axios.get('/fronted/mostrar_pelicula')
    .then(function(response) {
      var peliculas = response.data;
      var tableBody = document.getElementById('peliculas-lista');

      peliculas.forEach(function(pelicula) {
        var row = document.createElement('tr');

        var idCell = document.createElement('td');
        idCell.innerText = pelicula.id; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(idCell);

        var tituloCell = document.createElement('td');
        tituloCell.innerText = pelicula.titulo; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(tituloCell);

        var generoCell = document.createElement('td');
        generoCell.innerText = pelicula.genero; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(generoCell);

        var duracionCell = document.createElement('td');
        duracionCell.innerText = pelicula.duracion; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(duracionCell);

        var sinopsisCell = document.createElement('td');
        sinopsisCell.innerText = pelicula.sinopsis; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(sinopsisCell);

        var directorCell = document.createElement('td');
        directorCell.innerText = pelicula.director; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(directorCell);

        var imagenCell = document.createElement('td');
        imagenCell.innerText = pelicula.imagen; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(imagenCell);

        var trailerCell = document.createElement('td');
        trailerCell.innerText = pelicula.video; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(trailerCell);

        tableBody.appendChild(row);
      });
    })
    .catch(function(error) {
      console.log('Error al obtener los datos:', error);
    });
}
