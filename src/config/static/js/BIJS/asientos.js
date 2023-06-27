// Función para auto-rellenar los campos no editables
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
const container = document.querySelector('#contenedor_asientos');
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
// Función para guardar los asientos
function saveAsientos() {
  const asientosSeleccionados = obtenerAsientosSeleccionados(); // Obtén los asientos seleccionados
  const idSala = document.getElementById('id_sala').value; // Obtén el ID de la sala
  const idFuncion = document.getElementById('id_funcion').value;

  if (asientosSeleccionados.length === 0) {
    alert('Debes seleccionar al menos un asiento.');
    return;
  }

  // Realizar una solicitud POST para cada asiento seleccionado
  asientosSeleccionados.forEach(function(asiento) {
    const url = '/fronted/save_asiento';

    const data = {
      id_sala: idSala,
      id_funcion: idFuncion,
      numero: asiento.numero,
      estado: 'seat sold'
    };

    axios.post(url, data)
      .then(function(response) {
        console.log('Asiento guardado:', response.data);
        const asientoGuardado = response.data.asiento;

        // Realizar acciones adicionales con el asiento guardado
        // Por ejemplo, actualizar la interfaz de usuario para reflejar el estado del asiento

        // Actualizar el estado del asiento en la interfaz de usuario
        const asientoElement = document.getElementById(asientoGuardado.id);
        asientoElement.classList.remove('seat');
        asientoElement.classList.add('seat-sold');

        // Realizar otras acciones necesarias
      })
      .catch(function(error) {
        console.error('Error al guardar el asiento:', error);
      });
  });

  // Agregar los parámetros de la URL al redireccionar
  const urlParams = new URLSearchParams();
  urlParams.set('movie', encodeURIComponent(document.getElementById('pelicula').value));

  // Redirigir al siguiente HTML con los parámetros de la URL
  window.location.href = 'CTicket?' + urlParams.toString();
}

// Función para guardar el ticket
function saveTicket() {
  const token = localStorage.getItem('token');
  if (!token) {
    console.error('No se encontró un token en el sessionStorage');
    alert('No se encontró un token en el sessionStorage. Por favor, inicia sesión nuevamente.'); // Mostrar mensaje de error al usuario
    return;
  }

  axios.get(`/fronted/obtener_id_usuario?token=${token}`)
    .then(function (response) {
      if (response.data.hasOwnProperty('id_usuario')) {
        const id_usuarios = response.data.id_usuario;
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

        axios.post('/fronted/guardar_tickets', ticketData) // Reemplaza '/ruta/guardar_tickets' con la ruta correcta para guardar los tickets
          .then(function (response) {
            console.log('Ticket guardado:', response.data);
            const compraId = response.data.id; // Obtén el ID de la compra guardada

            // Resto del código...

            // Redirigir al archivo "CTicket" con el ID de la compra en la URL
            localStorage.setItem('compraId', compraId);
          })
          .catch(function (error) {
            console.error('Error al guardar el ticket:', error);
            alert('Hubo un error al guardar el ticket. Por favor, intenta nuevamente.'); // Mostrar mensaje de error al usuario
          });
      } else {
        console.error('No se pudo obtener el ID del usuario');
        alert('No se pudo obtener el ID del usuario. Por favor, intenta nuevamente.'); // Mostrar mensaje de error al usuario
      }
    })
    .catch(function (error) {
      console.error('Error al obtener el ID del usuario:', error);
      alert('Hubo un error al obtener el ID del usuario. Por favor, intenta nuevamente.'); // Mostrar mensaje de error al usuario
    });
}

//Guardar compra
// Obtén una referencia al formulario
const ticketForm = document.getElementById('ticketForm');

// Agrega un evento de escucha para el evento de envío del formulario
ticketForm.addEventListener('submit', function (e) {
  e.preventDefault(); // Evita el envío del formulario

  // Resto del código...

  // Guardar el ticket
  saveTicket();
});
