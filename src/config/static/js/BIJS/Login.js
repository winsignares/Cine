function valuesUser() {
    const Email = document.getElementById('EmailUser').value
    const Password = document.getElementById('PassUser').value

    console.log("getData.Email:'",Email,"'.and.Password:'",Password,"'")
    console.log("Validando User|...")

    axios.post('/fronted/validarUsuarioslg',{
        correo_electronico : Email,
        contrasena : Password
    })
    
    .then(function(res){ 
        const route = res.data.nav
        const userid = res.data.userid
        const rol = res.data.rol
        localStorage.setItem("userId", userid)
        alert("User id:",userid,"rol:",rol)
        window.location.href = route
    })
    .catch((err) => {
        console.log(err);
    })
}
function valuesRegister() {
    const NameUsuario = document.getElementById('Nombre_user').value;
    const RolUsuario = document.getElementById('Rol_user').value;
    const EmailUsuario = document.getElementById('Correo_user').value;
    const PassUsuario = document.getElementById('Contrasena_user').value;

    console.log("Validando Usuarios - Registro|...")
    console.log("Email:",EmailUsuario,"Password:",PassUsuario);

    axios.post('/fronted/savexUsuariosrg',{
        nombre: NameUsuario,
        Rol: RolUsuario,
        correo_electronico: EmailUsuario,
        contrasena : PassUsuario
    })    
    .then((res) => {
        alert("OK")
        console.log(res.data)
        window.location.href = res.data
    })
    .catch((err) => {
        console.log(err);
    })
}