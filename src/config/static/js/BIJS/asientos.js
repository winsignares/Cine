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

function genPDF() {
    var doc = new jsPDF();
    var container = document.getElementById('contenedor_ticket');
    doc.fromHTML(container.innerHTML, 15, 15, {
        'width': 170,
      });
    doc.save('saveus.pdf')
  
  }