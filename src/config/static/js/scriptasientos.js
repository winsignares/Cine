// Obtener elementos del DOM
const container = document.querySelector('#contenedor_asietos');
const seats = container.querySelectorAll('.seat');
const movieSelect = container.querySelector('#movie');

// Variables de seguimiento
let selectedSeats = [];

// Función para actualizar el contador de asientos seleccionados
function updateSelectedCount() {
  const selectedCount = selectedSeats.length;
  console.log(selectedCount);
}

// Evento de click en el asiento
container.addEventListener('click', (e) => {
  if (
    e.target.classList.contains('seat') &&
    !e.target.classList.contains('sold')
  ) {
    e.target.classList.toggle('selected');

    const seatIndex = [...seats].indexOf(e.target);
    if (selectedSeats.includes(seatIndex)) {
      selectedSeats = selectedSeats.filter((seat) => seat !== seatIndex);
    } else {
      selectedSeats.push(seatIndex);
    }

    updateSelectedCount();
  }
});

// Evento de cambio en la selección de película
movieSelect.addEventListener('change', (e) => {
  // Aquí puedes realizar cualquier acción cuando cambie la selección de película
});

// Variables globales
var botonesAsientos = document.querySelectorAll('.asiento');
var botonComprar = document.querySelector('.comprar');

// Agregar un evento de clic al botón de "Comprar"
botonComprar.addEventListener('click', function() {
  var botonesSeleccionados = document.querySelectorAll('.asiento-seleccionado');

  // Verificar si se han seleccionado asientos
  if (botonesSeleccionados.length > 0) {
    // Obtener información de los asientos seleccionados
    var asientosSeleccionados = [];
    botonesSeleccionados.forEach(function(botonSeleccionado) {
      var fila = botonSeleccionado.dataset.fila;
      var asiento = botonSeleccionado.dataset.asiento;
      asientosSeleccionados.push({fila: fila, asiento: asiento});
    });

    // Enviar información a un servidor utilizando Axios
    axios.post('/guardar-asientos', {
      asientos: asientosSeleccionados
    })
    .then(function(response) {
      console.log(response);
    })
    .catch(function(error) {
      console.log(error);
    });
  }
});

// Agregar un evento de clic a cada botón de asiento
botonesAsientos.forEach(function(botonAsiento) {
  botonAsiento.addEventListener('click', function() {
    // Cambiar la clase del botón para reflejar el estado de selección
    if (botonAsiento.classList.contains('asiento-seleccionado')) {
      botonAsiento.classList.remove('asiento-seleccionado');
      botonAsiento.textContent = botonAsiento.dataset.asiento;
    } else if (botonAsiento.classList.contains('asiento-ocupado')) {
      // El asiento ya está ocupado, no se puede seleccionar
      return;
    } else {
      botonAsiento.classList.add('asiento-seleccionado');
      botonAsiento.textContent = 'X';
    }
    
    // Verificar si se han seleccionado asientos para habilitar/deshabilitar el botón de "Comprar"
    var botonesSeleccionados = document.querySelectorAll('.asiento-seleccionado');
    if (botonesSeleccionados.length > 0) {
      botonComprar.disabled = false;
    } else {
      botonComprar.disabled = true;
    }
  });
});
