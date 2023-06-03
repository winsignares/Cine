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

// Función para obtener información de los asientos seleccionados
function getSelectedSeats() {
  const selectedSeatsInfo = [];
  seats.forEach((seat, indexAsiento) => {
    if (seat.classList.contains('selected')) {
      const seatInfo = {
        id_sala: movieSelect.value,
        numero: seat.dataset.seatNumber,
        estado: 'seleccionado'
      };
      selectedSeatsInfo.push(seatInfo);
    }
  });
  return selectedSeatsInfo;
}

// Función para guardar la información de los asientos en la base de datos
function guardarAsientos() {
  const asientosSeleccionados = getSelectedSeats();
  if (asientosSeleccionados.length > 0) {
    axios.post('/save_asientos', asientosSeleccionados)
      .then(function (response) {
        console.log(response.data.message);
        // Actualizar el HTML para reflejar el estado de los asientos en la base de datos
      })
      .catch(function (error) {
        console.log(error);
      });
  }
}

// Evento de click en el botón "Generar Ticket"
const generarTicketButton = document.querySelector('#generarTicket');
generarTicketButton.addEventListener('click', function (e) {
  e.preventDefault();
  guardarAsientos();
});

// Función para obtener los asientos de la base de datos y actualizar el HTML
function obtenerAsientosDeBD() {
  axios.get('/asientos/' + movieSelect.value)
    .then(function (response) {
      const asientos = response.data;
      asientos.forEach((asiento) => {
        const seatIndex = parseInt(asiento.numero) - 1;
        seats[seatIndex].classList.add('sold');
      });
    })
    .catch(function (error) {
      console.log(error);
    });
}

// Obtener los asientos de la base de datos al cargar la página
obtenerAsientosDeBD();
