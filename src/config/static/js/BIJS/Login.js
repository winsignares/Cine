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
        console.log("Res: ", res)
        localStorage.setItem("userId", res.data)
        console.log(res.data);
        //window.location.href = res.data
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

    axios.post('/fronted/validarUsuariosrg',{
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
function toggleDropdown() {
    var dropdown = document.getElementById("dropdown-menu");
    dropdown.classList.toggle("show");
}
window.onclick = function(event) {
    if (!event.target.matches(".user-name")) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains("show")) {
                openDropdown.classList.remove("show");
        }
      }
    }
};