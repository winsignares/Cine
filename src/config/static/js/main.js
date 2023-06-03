// Capturar el formulario por su ID
var form = document.getElementById('formulario');

// Agregar un evento para escuchar el envío del formulario
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Evitar el envío por defecto

  // Obtener los valores de los campos del formulario
  var id = document.getElementById('id').value;
  var titulo = document.getElementById('titulo').value;
  var genero = document.getElementById('genero').value;
  var duracion = document.getElementById('duracion').value;
  var sinopsis = document.getElementById('sinopsis').value;
  var director = document.getElementById('director').value;
  var imagen = document.getElementById('imagen').value;

  // Crear una nueva fila en la tabla
  var tableBody = document.getElementById('peliculas-lista');
  var newRow = tableBody.insertRow();
  newRow.innerHTML = `
    <td>${id}</td>
    <td>${titulo}</td>
    <td>${genero}</td>
    <td>${duracion}</td>
    <td>${sinopsis}</td>
    <td>${director}</td>
    <td>${imagen}</td>
  `;

  // Limpiar los campos del formulario
  form.reset();
});

