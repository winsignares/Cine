//PRUEBA: Esto es un metodo para cargar el contenido del archivo HTML del servidor.
window.addEventListener('DOMContentLoaded', function() {
    var contenidoExterno = document.getElementById('contenidoExterno');
    fetch('ruta/del/archivo.html') // Reemplaza 'ruta/del/archivo.html' con la ruta correcta del archivo HTML externo
    .then(response => response.text())
    .then(data => {
        contenidoExterno.innerHTML = data;
    })
    .catch(error => {
        console.log('Error:', error);
    });
});
function addPelis() {
    alert("OK")
    const titleHTML = document.getElementById('titlePelis')
    const remplazoHTML = document.createElement('h1')
    axios.get('/mostrar',{
        responseType: 'json'
    })
    .then(function(res) {
        let datos = res.data
        //var length = (Object.keys(datos).length) +1;
        let opciones = "El juego del calamar2";
        /*for (let index = 1; index < length; index++) {
            opciones += `
                <h1 id="titlePelis" class='view__title'>El juego del calamar
                <span>(2021)</span></h1>
            `
        }*/
        //remplazoHTML.innerHTML = titleHTML.innerHTML;
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