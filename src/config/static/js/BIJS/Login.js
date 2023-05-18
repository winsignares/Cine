function valuesUser() {
    const Email = document.getElementById('EmailUser').value
    const Password = document.getElementById('PassUser').value

    console.log("getData.Email:'",Email,"'.and.Password:'",Password,"'")

    console.log("Validando User|...")
    axios.post('/fronted/validarUsuarioslg',{
        email : Email,
        password : Password
    })
    
    .then(function(res){
        
        console.log(res.data);
        window.location.href = res.data

    })

    .catch((err) => {
        console.log(err);
    })
}
function valuesRegister() {
    const NameUsuario = document.getElementById('NameUser').value;
    const RolUsuario = document.getElementById('RolUser').value;
    const EmailUsuario = document.getElementById('EmailUser').value;
    const PassUsuario = document.getElementById('PassUser').value;

    console.log("Validando Usuarios - Registro|...")
    console.log("Email:",EmailUsuario,"Password:",PassUsuario);

    axios.post('/fronted/validarUsuariosrg',{
        nombre: NameUsuario,
        correo_electronico: EmailUsuario,
        contrasena : PassUsuario
    })
    
    .then((res) => {
        console.log(res.data)
    })
    .catch((err) => {
        console.log(err);
    })
}