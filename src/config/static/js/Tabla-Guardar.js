/*// Capturar el formulario por su ID
var form = document.getElementById('formulario');
// 

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
});*/
function showAllPeliculas() {
  axios.get("/showAdmin", {
      id: id,
      titulo: titulo,
      genero: genero,
      duracion: duracion,
      sinopsis: sinopsis,
      director: director,
      imagen: imagen,
    })
    .then(function (res) {
      datos = res.data;
      console.log(res.datos);
      // Crear una nueva fila en la tabla
      var tableBody = document.getElementById("peliculas-lista");
      var newRow = tableBody.insertRow();
      newRow.innerHTML = `
        <td>${datos.id}</td>
        <td>${datos.titulo}</td>
        <td>${datos.genero}</td>
        <td>${datos.duracion}</td>
        <td>${datos.sinopsis}</td>
        <td>${datos.director}</td>
        <td>${datos.imagen}</td>
      `;

      // Limpiar los campos del formulario
      form.reset();
    })
    .catch((err) => {
      console.log(err);
    });
}
function sendNewPeliculas() {
  // Obtener los valores de los campos del formulario
  var id = document.getElementById("id").value;
  var titulo = document.getElementById("titulo").value;
  var genero = document.getElementById("genero").value;
  var duracion = document.getElementById("duracion").value;
  var sinopsis = document.getElementById("sinopsis").value;
  var director = document.getElementById("director").value;
  var imagen = document.getElementById("imagen").value;

  axios.post("/saveAdmin", {
      id: id,
      titulo: titulo,
      genero: genero,
      duracion: duracion,
      sinopsis: sinopsis,
      director: director,
      imagen: imagen,
    })
    .then(function (res) {
      datos = res.data;
      console.log(res.datos);
      //showAllPeliculas(datos)
      // Crear una nueva fila en la tabla
      var tableBody = document.getElementById("peliculas-lista");
      var newRow = tableBody.insertRow();
      newRow.innerHTML = `
        <td>${datos.id}</td>
        <td>${datos.titulo}</td>
        <td>${datos.genero}</td>
        <td>${datos.duracion}</td>
        <td>${datos.sinopsis}</td>
        <td>${datos.director}</td>
        <td>${datos.imagen}</td>
      `;

      // Limpiar los campos del formulario
      //form.reset();
    })
    .catch((err) => {
      console.log(err);
    });
}
/*/ Capturar el formulario por su ID
var form = document.getElementById("formulario");
//

// Agregar un evento para escuchar el envío del formulario
form.addEventListener("click", function (event) {
  event.preventDefault(); // Evitar el envío por defecto
  sendNewPeliculas();
});/*/
