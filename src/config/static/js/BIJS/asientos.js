  function autoRellenarInputsNoEditables() {
    const urlParams = new URLSearchParams(window.location.search);
    const peli = urlParams.get('movie');
  
    axios.get(`/fronted/buscarfunciones?titulo=${peli}`)
      .then(function (response) {
        const tickets = response.data;
  
        if (tickets.length > 0) {
          const ticket = tickets[0];
  
          document.getElementById('id_sala').value = ticket.id_sala;
          document.getElementById('id_funcion').value = ticket.id;
          document.getElementById('pelicula').value = peli;
        }
      })
      .catch(function (error) {
        console.error('Error al obtener los datos del ticket:', error);
      });
  }
  
  window.onload = autoRellenarInputsNoEditables;

  // Asientos
  const container = document.querySelector('#contenedor_asietos');
  const seats = container.querySelectorAll('.seat');
  const movieSelect = container.querySelector('#movie');
  const asientosElement = document.getElementById('asientos');
  
  // Variables de seguimiento
  let selectedSeats = [];
  
  // Función para actualizar el contador de asientos seleccionados y el total
  function updateSelectedCount() {
    const selectedCount = selectedSeats.length;
    const total = selectedCount * 5000;
  
    // Actualizar el valor total en el campo de entrada
    document.getElementById('total').value = total;
  
    // Actualizar el contador de asientos
    asientosElement.textContent = selectedCount;
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
  
//Guardar compra
// Obtén una referencia al formulario
const ticketForm = document.getElementById('ticketForm');

// Agrega un evento de escucha para el evento de envío del formulario
ticketForm.addEventListener('submit', function (event) {
  event.preventDefault(); // Evita que el formulario se envíe y recargue la página
  saveTicket(); // Guarda el ticket utilizando Axios
});

// Función para guardar el ticket
function saveTicket() {
  const id_usuarios = 1; // Aquí debes obtener el ID del usuario de alguna manera
  const id_funcion = document.getElementById('id_funcion').value;
  const cantidad_tickets = selectedSeats.length;
  const total_pagado = document.getElementById('total').value;
  const fecha_compra = new Date().toISOString(); // Fecha actual

  const ticketData = {
    id_usuarios,
    id_funcion,
    cantidad_tickets,
    total_pagado,
    fecha_compra,
  };

  axios.post('/fronted/save_compras', ticketData)
    .then(function (response) {
      console.log('Ticket guardado:', response.data);
      // Realizar acciones adicionales después de guardar el ticket, si es necesario
    })
    .catch(function (error) {
      console.error('Error al guardar el ticket:', error);
    });
}

