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
