//PRUEBA: Esto es un metodo para cargar el contenido HTML-descripcion de otro archivo HTML con datos del servidor.
window.addEventListener('DOMContentLoaded', function() {
    var contenidoExterno = document.getElementById('titlePelis');
    fetch('.') // Aqui debe ir la ruta correcta del archivo HTML externo
    .then(response => response.text())
    .then(data => {
        contenidoExterno.innerHTML = data;
    })
    .catch(error => {
        console.log('Error:', error);
    });
});//-Finish---------------------------------------------------------------
function addPelis() {
    alert("OK")
    const titleHTML = document.getElementById('titlePelis')
    axios.get('/mostrar',{
        responseType: 'json'
    })
    .then(function(res) {
        let datos = res.data
        var length = (Object.keys(datos).length) +1;
        let opciones = "El juego del calamar2";
        for (let index = 1; index < length; index++) {
            opciones += `
                <h1 id="titlePelis" class='view__title'>El juego del calamar
                <span>(2021)</span></h1>
            `
        }
        titleHTML.innerHTML = opciones;
        window.location.href = 'indexDescripcion'
        alert("Here?")
    })
    .catch(function(error) {
        console.log(error);
    })
}
/**Este es un metodo para cargar las imagenes del servidor.
 * Imagenes
 * <script src="{{url_for('static', filename='/asets/imagenes/${nameImg}.png')}}"></script>
 * Categoria - las carpetas tendran nombres de la categoria de las peliculas
 * <script src="{{url_for('static', filename='/asets/${nameCarp}/${nameImg}.png')}}"></script>
 */