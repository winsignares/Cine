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
  
  window.onload = autoRellenarInputsNoEditables;

   // Lógica JavaScript para obtener y mostrar los asientos comprados
   document.addEventListener('DOMContentLoaded', () => {
    const userId = 1; // ID del usuario
    const funcionId = 2; // ID de la función

    const obtenerAsientosComprados = async () => {
        try {
            const response = await axios.get('/asientos_comprados', {
                params: {
                    user_id: userId,
                    funcion_id: funcionId
                }
            });

            const asientosComprados = response.data;

            const ticketDetails = document.getElementById('ticketDetails');

            asientosComprados.forEach(asiento => {
                const card = document.createElement('div');
                card.classList.add('card');

                const cardBody = document.createElement('div');
                cardBody.classList.add('card-body');

                const cardTitle = document.createElement('h5');
                cardTitle.classList.add('card-title');
                cardTitle.textContent = `Asiento ID: ${asiento.id}`;

                const cardText1 = document.createElement('p');
                cardText1.classList.add('card-text');
                cardText1.textContent = `Número: ${asiento.numero}`;

                const cardText2 = document.createElement('p');
                cardText2.classList.add('card-text');
                cardText2.textContent = `Estado: ${asiento.estado}`;

                cardBody.appendChild(cardTitle);
                cardBody.appendChild(cardText1);
                cardBody.appendChild(cardText2);

                card.appendChild(cardBody);

                ticketDetails.appendChild(card);
            });

            // Mostrar el resultado de los asientos comprados
            const ticketResult = document.getElementById('ticketResult');
            ticketResult.style.display = 'block';

        } catch (error) {
            console.error('Error al obtener los asientos comprados:', error);
        }
    };

    const ticketForm = document.getElementById('ticketForm');
    ticketForm.addEventListener('submit', event => {
        event.preventDefault();
        obtenerAsientosComprados();
    });
});