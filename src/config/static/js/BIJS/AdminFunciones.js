function sendNewFunciones() {
  // Obtener los valores de los campos del formulario
  var id = document.getElementById('id').value;
  var id_pelicula = document.getElementById('IDPelicula').value;
  var id_sala = document.getElementById('IDSala').value;
  var fecha = document.getElementById('fecha').value;
  var precio = document.getElementById('precio').value;


  // Crear un objeto con los datos de la película
  var funcion = {
    id: id,
    id_pelicula: id_pelicula,
    id_sala: id_sala,
    fecha: fecha,
    precio: precio
  };

  // Realizar la solicitud POST al endpoint '/saveAdmin' en el servidor
  fetch('/fronted/saveFuncion', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(funcion)
  })
    .then(response => {
      if (response.ok) {
        // La película se guardó exitosamente
        alert('La funcion se ha guardado correctamente');
      } else {
        // Ocurrió un error al guardar la película
        alert('Error al guardar la funcion');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
window.onload = function () {
  cargarDatosTabla();
};

function cargarDatosTabla() {
  axios.get('/fronted/mostrar_funciones')
    .then(function (response) {
      var funciones = response.data;
      var tableBody = document.getElementById('funciones-lista');

      funciones.forEach(function (funcion) {
        var row = document.createElement('tr');

        var idCell = document.createElement('td');
        idCell.innerText = funcion.id; // Asegúrate de utilizar el nombre de la propiedad correcto
        row.appendChild(idCell);

        var idPeliculaCell = document.createElement('td');
        idPeliculaCell.innerText = funcion.idPelicula;
        row.appendChild(idPeliculaCell);

        var idSalaCell = document.createElement('td');
        idSalaCell.innerText = funcion.idSala;
        row.appendChild(idSalaCell);

        var fechaCell = document.createElement('td');
        fechaCell.innerText = funcion.fecha;
        row.appendChild(fechaCell);

        var precioCell = document.createElement('td');
        precioCell.innerText = funcion.precio;
        row.appendChild(precioCell);

        tableBody.appendChild(row);
      });
    })
    .catch(function (error) {
      console.error('Error:', error);
    });
}
