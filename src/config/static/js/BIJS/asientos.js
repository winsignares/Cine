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
  seats.forEach((seat, index) => {
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
    axios.post('/fronted/save_asientos', asientosSeleccionados)
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
  axios.get('/fronted/asientos/' + movieSelect.value)
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
window.onload = obtenerAsientosDeBD();



// Función para autorellenar los campos del formulario
function autoRellenarFormulario() {
  // Obtener el nombre de la película de la URL
  const urlParams = new URLSearchParams(window.location.search);
  const movieName = urlParams.get('movie');

  axios.get('/fronted/mostrarticket')
    .then(function (response) {
      // Obtener los datos de la respuesta
      const tickets = response.data;

      // Buscar el ticket correspondiente al nombre de la película
      const ticket = tickets.find((t) => t.titulo.toLowerCase() === movieName.toLowerCase());

      if (ticket) {k
        // Rellenar los campos del formulario con los datos del ticket
        document.getElementById('pelicula').value = ticket.titulo;
        document.getElementById('sala').value = ticket.sala;
        document.getElementById('funcion').value = ticket.fecha;
      }
    })
    .catch(function (error) {
      console.error('Error al obtener los datos del ticket:', error);
    });
    window.onload = autoRellenarFormulario;
}

// Ejecutar la función de autorellenado al cargar la página


// Manejar el envío del formulario
document.getElementById('ticketForm').addEventListener('submit', function (event) {
  event.preventDefault();
  // Aquí puedes agregar la lógica para generar el ticket
  // y mostrarlo en el elemento con el ID "ticketDetails"
  const asientos = document.getElementById('asientos').value;
  const metodoPago = document.getElementById('metodoPago').value;
  const total = document.getElementById('total').value;
  const ticketDetails = document.getElementById('ticketDetails');
  ticketDetails.innerHTML = `
    <p>Asientos: ${asientos}</p>
    <p>Método de Pago: ${metodoPago}</p>
    <p>Total por Asiento: ${total}</p>
  `;
  document.getElementById('ticketResult').style.display = 'block';
});

function genPDF() {
    var doc = new jsPDF();
    var container = document.getElementById('contenedor_ticket');
    doc.fromHTML(container.innerHTML, 15, 15, {
        'width': 170,
      });
    doc.save('saveus.pdf')
  
  }