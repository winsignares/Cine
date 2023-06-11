document.addEventListener("DOMContentLoaded", function() {
    const idSalaInput = document.getElementById('id_sala');
    const idFuncionInput = document.getElementById('id_funcion');
    const mostrarAsientosButton = document.getElementById('mostrar_asientos_button');
  
    mostrarAsientosButton.addEventListener("click", function() {
      const idSala = idSalaInput.value;
      const idFuncion = idFuncionInput.value;
  
      mostrarAsientosSeleccionados(idSala, idFuncion);
    });
  
    // Autoclic después de un tiempo de espera
    setTimeout(function() {
      mostrarAsientosButton.click();
    }, 1000); // Espera 1 segundo antes de hacer clic en el botón
  
    function mostrarAsientosSeleccionados(idSala, idFuncion) {
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
  });
  