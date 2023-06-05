  // Obtener el título de la película del elemento HTML
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

function obtenerTituloDeURL() {
    const url = window.location.href;
    const urlParams = new URL(url);
    const titulo = urlParams.searchParams.get('titulo');
    return titulo;
  }
  


// Descricion  
function autoRellenardesc() {
    // Obtener el título de la película de la URL
    const urlParams = new URLSearchParams(window.location.search);
    const titulo = obtenerTituloDeURL()
  
    // Realizar una solicitud GET al servidor para obtener los datos de la película
    axios.get(`/fronted/mostrarpelidesc?titulo=${titulo}`, {
        ResponseType: 'json'
    })
      .then(function (response) {
        // Obtener los datos de la respuesta
        let datos = response.data;
        var length = (Object.keys(datos).length) + 1;
        let opciones = '';
        for (let indexDescripcion = 1; indexDescripcion < length; indexDescripcion ++ ){

            opciones +=`
            <div class='container movie__overview'>
    <div class='container movie__overview-wrapper'>
    <div class='backdrop__container'>
    <img alt='' class='backdrop__image' src='https://1.bp.blogspot.com/-YXpj5ooaK5w/YVhgR7HDCmI/AAAAAAAACbE/6-sQgaAlWDo9Cg3JkzTH22Go0RX65TcKwCLcBGAsYHQ/s1155/BrowserPreview_tmp.png'/>
    </div>
    <div class='view'>
    <div class='view__wrapper'>
    <div class='view__poster'>
    <img id="imagen" src='${datos[indexDescripcion].imagen}'/>
    </div>
    <div class='view__details'>
    <h1 id="titlePelis" class='view__title'>
    <span></span></h1>
    <p class='view__info mb-0'>
    <i class='fa fa-star'></i>&nbsp;8.1   &nbsp;&nbsp;
    <i id="duracion" class='fa fa-clock'></i>&nbsp; 
    </p>${datos[indexDescripcion].duracion}
    <p id="genero" class='mt-0 text-subtle'>
    <span>${datos[indexDescripcion].genero}</span> /
    <span>.</span> /
    <span>.</span> /
    <span>.</span>
    </p>
    <p id="sinopsis" class='view__overview'>${datos[indexDescripcion].sinopsis}</p>
    <div class='view__actions'> 
    <button id="Trailer" class="button--primary"><a href="#TrailerShow" >Ver Trailer &nbsp;&nbsp;<i class='fa fa-play'></i></a></button>&nbsp;
    <button class='button--download' >
    <a href='' onclick="redirectToIndexAsientos()" >Obtener Ticket&nbsp;&nbsp;<i class='fa fa-download'></i></a>
    </button>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div id="TrailerShow" class='container__wrapper'>
    <div id='main__player'>
    <div class='flex__center watch__title'>
    <h1 class='flex__center'>Trailer</h1>
    <div  class="text-center">
        <option id="video" value='${datos[indexDescripcion].video}' class="rounded"></option>
    </div>
    </select>
    </div>
    <iframe id="video" allowfullscreen='' frameborder='0' height='600' id='main__iframe' name='main__iframe' playsinline='' scrolling='no' src='${datos[indexDescripcion].video}' width='100%'></iframe>
    </div>
    </div>`
        }
  
      })
      .catch(function (error) {
        console.error('Error al obtener los datos de la película:', error);
      });
  }
  
  window.onload = autoRellenardesc();
