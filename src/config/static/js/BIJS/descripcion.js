function addPelis() {
    alert("OK")
    const remplazoHTML = document.getElementById('descripcionRemplazo')
    axios.get('/mostrar',{
        responseType: 'json'
    })
    .then(function(res) {
        let datos = res.data
        var length = (Object.keys(datos).length) +1;
        let opciones = "";
        for (let index = 1; index < length; index++) {
            opciones += `
            <div class='container movie__overview'>
            <div class='container movie__overview-wrapper'>
            <div class='backdrop__container'>
            <img alt='' class='backdrop__image' src='https://1.bp.blogspot.com/-YXpj5ooaK5w/YVhgR7HDCmI/AAAAAAAACbE/6-sQgaAlWDo9Cg3JkzTH22Go0RX65TcKwCLcBGAsYHQ/s1155/BrowserPreview_tmp.png'/>
            </div>
            <div class='view'>
            <div class='view__wrapper'>
            <div class='view__poster'>
            <img src='https://1.bp.blogspot.com/-czSrv2lPcLI/YVhdk6KbBII/AAAAAAAACa8/uVpivcpztHAuTMQBVSQiDz31P2MU8QntQCLcBGAsYHQ/s889/yvW9VuHiwfAaTNYjALROI8evNIT.jpg'/>
            </div>
            <div class='view__details'>
            <h1 class='view__title'>El juego del calamar
            <span>(2021)</span></h1>
            <p class='view__info mb-0'>
            <i class='fa fa-star'></i>&nbsp;8.1   &nbsp;&nbsp;
            <i class='fa fa-clock'></i>&nbsp; 50m
            </p>
            <p class='mt-0 text-subtle'>
            <span>Serie</span> /
            <span>Acción</span> /
            <span>Aventura</span> /
            <span>Misterio</span>
            </p>
            <p class='view__overview'>Cientos de jugadores con problemas de dinero aceptan una invitación rarísima para competir en juegos infantiles. Dentro les esperan un tentador premio y desafíos letales.</p>
            <div class='view__actions'> 
            <button id="Trailer" class="button--primary"><a href="#TrailerShow" >Ver Trailer &nbsp;&nbsp;<i class='fa fa-play'></i></a></button>&nbsp;
            <button class='button--download'>
            <a href='https://ouo.io/V0Akdu' target='_blank'>Optener Ticket&nbsp;&nbsp;<i class='fa fa-download'></i></a>
            </button>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            <div id="TrailerShow" class='container__wrapper'>
            <div id='main__player'>
            <div class='flex__center watch__title'>
            <h1 class='flex__center'>Mondongo</h1>
            <div  class="text-center">
                <option value='https://www.youtube.com/embed/Mj4_xG5NXeo' class="rounded">Opción 1</option>
            </div>
            </select>
            </div>
            <iframe allowfullscreen='' frameborder='0' height='600' id='main__iframe' name='main__iframe' playsinline='' scrolling='no' src='https://www.youtube.com/embed/Mj4_xG5NXeo' width='100%'></iframe>
            </div>
            </div>
            `
        }
        remplazoHTML.innerHTML = opciones;
        window.location.href = "indexDescripcion"
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