function addPelis() {
    // Obtener el título de la película
    const titulopelicula = event.target.closest('.movie-item').querySelector('.movie-item-title').textContent.trim();
  
    // Codificar el título de la película para incluirlo en la URL
    var url = '/fronted/indexDescripcion?movie=' + encodeURIComponent(titulopelicula);
    // Redirigir a la página indexAsientos con el título de la película en la URL
    window.location.href = url
  }