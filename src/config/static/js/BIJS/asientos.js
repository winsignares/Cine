const pelicula = document.getElementById('pelicula');
const sala = document.getElementById('sala');
const funcion = document.getElementById('funcion');

function mostrarTicket() {
axios.get('/mostrarticket',{
    responseType: 'json'
})  

.then (funcion(response)
)
}