function imprimirTickets(tickets) {
    const ticketDetails = document.getElementById("ticketDetails");
    ticketDetails.innerHTML = "";
  
    for (let i = 0; i < tickets.length; i++) {
      const ticket = tickets[i];
      
      const ticketInfo = document.createElement("div");
      ticketInfo.classList.add("ticket-info");
  
      const ticketId = document.createElement("p");
      ticketId.textContent = "ID del Ticket: " + ticket.id;
  
      const compraId = document.createElement("p");
      compraId.textContent = "ID de la Compra: " + ticket.id_compra;
  
      const funcionId = document.createElement("p");
      funcionId.textContent = "ID de la Función: " + ticket.id_funcion;
  
      const asientoId = document.createElement("p");
      asientoId.textContent = "ID del Asiento: " + ticket.id_asiento;
  
      const fechaEmision = document.createElement("p");
      fechaEmision.textContent = "Fecha de Emisión: " + ticket.fecha_emision;
  
      ticketInfo.appendChild(ticketId);
      ticketInfo.appendChild(compraId);
      ticketInfo.appendChild(funcionId);
      ticketInfo.appendChild(asientoId);
      ticketInfo.appendChild(fechaEmision);
  
      ticketDetails.appendChild(ticketInfo);
    }
  
    const ticketResult = document.getElementById("ticketResult");
    ticketResult.style.display = "block";
  }

  const ticketForm = document.getElementById("ticketForm");

ticketForm.addEventListener("submit", function(event) {
  event.preventDefault();

  const idUsuario = document.getElementById("id_usuario").value;
  const idCompra = document.getElementById("id_compra").value;

  // Realiza la solicitud GET al servidor
  axios.get(`/crear_ticketes?id_usuario=${idUsuario}&id_compra=${idCompra}`)
    .then(response => {
      const tickets = response.data;
      
      // Imprime los tickets
      imprimirTickets(tickets);
    })
    .catch(error => {
      console.error(error);
    });
});

function autoRellenarUsuario() {
    // Verificar si el token está almacenado en el localStorage
    if (localStorage.getItem("token")) {
      // Obtener el token del localStorage
      const token = localStorage.getItem("token");
  
      // Decodificar el token para obtener el ID de usuario
      const decodedToken = jwt_decode(token);
  
      // Obtener el ID de usuario del token decodificado
      const idUsuario = decodedToken.id_usuario;
  
      // Rellenar el campo de ID de usuario en el formulario
      const usuarioInput = document.getElementById("id_usuario");
      usuarioInput.value = idUsuario;
    }
  }
  
  // Llamar a la función para auto-rellenar el campo de usuario al cargar la página
  window.addEventListener("DOMContentLoaded", autoRellenarUsuario);
  