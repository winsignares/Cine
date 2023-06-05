
// Obtener el título de la película desde el elemento HTML
var movieTitle = document.getElementById('titlePelis').textContent.trim();

// Función para redirigir a indexAsientos con el nombre de la película en la URL
function redirectToIndexAsientos() {
  var url = 'indexAsientos?movie=' + encodeURIComponent(movieTitle);
  window.location.href = url;
}

// Asignar la función al botón "Obtener Tickets"
var obtenerTicketsButton = document.querySelector('.button--download');
obtenerTicketsButton.addEventListener('click', redirectToIndexAsientos);



/**Este es un metodo para cargar las imagenes del servidor.
 * Imagenes
 * <script src="{{url_for('static', filename='/asets/imagenes/${nameImg}.png')}}"></script>
 * Categoria - las carpetas tendran nombres de la categoria de las peliculas
 * <script src="{{url_for('static', filename='/asets/${nameCarp}/${nameImg}.png')}}"></script>
 */

// Descricion  

  function autoRellenarHTML(datos) {
    document.getElementById('imagen').src = datos.imagen;
    document.getElementById('titlePelis').textContent = datos.titulo;
    document.getElementById('duracion').textContent = datos.duracion;
    document.getElementById('genero').getElementsByTagName('span')[0].textContent = datos.genero;
    document.getElementById('sinopsis').textContent = datos.sinopsis;
    document.getElementById('video').value = datos.video;
  }
  
  function autoRellenarFormulario() {
    const url = window.location.href;
    const urlParams = new URL(url);
    const movie = urlParams.searchParams.get('movie');
  
    axios.get(`/fronted/mostrarpelidesc?titulo=${movie}`)
      .then(function (response) {
        const datos = response.data;
        autoRellenarHTML(datos);
      })
      .catch(function (error) {
        console.error('Error al obtener los datos de la película:', error);
      });
  }
  
  window.onload = autoRellenarFormulario;
  
