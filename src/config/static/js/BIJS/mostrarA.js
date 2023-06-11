
  

function mostrarAsientosSeleccionados() {
    const idSala = document.getElementById('id_sala').value;
    const idFuncion = document.getElementById('id_funcion').value;
  
    axios.get(`/fronted/mostrar_asientos/?id_sala=${idSala}&id_funcion=${idFuncion}`)
      .then(function(response) {
        const asientos = response.data;
        asientos.forEach(function(asiento) {
          const asientoElement = document.getElementById(asiento.numero);
          if (asiento.estado === 'seat sold') {
            asientoElement.className = 'seat sold';
          } else {
            asientoElement.className = 'seat';
          }
        });
      })
      .catch(function(error) {
        console.error('Error al obtener los asientos:', error);
      });
  }
  
  // Llamar a la función para mostrar los asientos seleccionados al cargar la página
  document.addEventListener("DOMContentLoaded", function() {
    mostrarAsientosSeleccionados();
  });