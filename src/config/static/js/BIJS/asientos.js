// Función para autorellenar los campos del formulario
function autoRellenarFormulario() {
  // Obtener el nombre de la película de la URL
  const urlParams = new URLSearchParams(window.location.search);
  const movieName = urlParams.get('movie');

  axios.get('/mostrarticket')
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
}

// Ejecutar la función de autorellenado al cargar la página
window.onload = autoRellenarFormulario;

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