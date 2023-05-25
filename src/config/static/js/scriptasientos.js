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