  function mostrarVideoDePelicula() {
    const url = window.location.href;
    const urlParams = new URL(url);
    const movie = urlParams.searchParams.get('movie');
    
    axios.get(`/fronted/mostrarpelidesc?titulo=${movie}`)
      .then(function (response) {
        var datos = response.data;
        autoRellenarHTML(datos);
  
        if (datos.video) {
          var div = document.getElementById('video'); // Reemplaza 'video' por el ID del div donde deseas mostrar el video
          var iframe = document.createElement('iframe');
          iframe.src = datos.video;
          iframe.width = '1280';
          iframe.height = '720';
          iframe.title = datos.titulo;
          iframe.frameBorder = '0';
          iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
          iframe.allowFullscreen = true;
          div.appendChild(iframe);
        } else {
          console.log('No se encontró el video de la película');
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  
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
        mostrarVideoDePelicula();
      })
      .catch(function (error) {
        console.error('Error al obtener los datos de la película:', error);
      });
  }
  
  window.onload = autoRellenarFormulario;

  
  function obtenerParametroDeURL(movie) {
    var urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(movie);
  }
  
  function redirectToIndexAsientos() {
    var movie = obtenerParametroDeURL('movie');
    var url = 'indexAsientos?movie=' + encodeURIComponent(movie);
    window.location.href = url;
  }
  const token = localStorage.getItem('token');