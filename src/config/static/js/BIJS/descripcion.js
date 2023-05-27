function addPelis() {
    axios.get('fronted/mostrar',{
        responseType: 'json'
    })
    .then(function(res) {
        let datos = res.data
        var length = (Object.keys(datos).length) +1;
        let opciones = ""
        for (let index = 1; index < length; index++) {
            const opciones =+ ``
        }
    })
    .catch(function(error) {
        console.log(error);
    })
}