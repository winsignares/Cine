function addPelis() {
    alert("OK")
    axios.get('/mostrar',{
        responseType: 'json'
    })
    .then(function(res) {
        let datos = res.data
        var length = (Object.keys(datos).length) +1;
        let opciones = ``
        for (let index = 1; index < length; index++) {
            opciones =+ ``
        }
        window.location.href = "fronted/indexDescripcion"
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