function mostrarTicket() {

    const pelicula = document.getElementById('pelicula');
    const sala = document.getElementById('sala');
    const funcion = document.getElementById('funcion');

    axios.get('/fronted/mostrarticket', {
        responseType: 'json',

    })

        .then(function (response) {
            let datos = response.data
            var lenght = (Object.keys(datos).length) + 1;
            let opciones = '';
            for (let index = 1; index < lenght; index++) {
                opciones += `
            <div class="card" id="contenedor_ticket">
      <title>Generador de Ticket de Cine</title>
      </style>
      <div class="container" id="formulario">
        <div class="card" id="formulario">
          <h3 class="card-title">Generador de Ticket de Cine</h3>
          <form id="ticketForm">
            <div class="form-group">
              <label for="pelicula">Película:</label>
              <input type="" class="form-control" id="pelicula" required>
            </div>
            <div class="form-group">
              <label for="sala">Sala:</label>
              <input type="text" class="form-control" id="sala" required>
            </div>
            <div class="form-group">
              <label for="funcion">Función:</label>
              <input type="text" class="form-control" id="funcion" required>
            </div>
            `
            }
        })
}
