function valuesUser() {
    const Email = document.getElementById('EmailUser').value;
    const Password = document.getElementById('PassUser').value;

    console.log("getData.Email:'", Email, "'.and.Password:'", Password, "'");

    console.log("Validando User|...");
    axios.post('/fronted/validarUsuarioslg', {
        correo_electronico: Email,
        contrasena: Password
    })
    .then(function(res) {
        const data = res.data;
        // Extraer solo el token de la ruta
        const token = extractTokenFromUrl(data.nav);
        // Guardar el token en el localStorage
        localStorage.setItem('token', token);
        console.log("Token guardado en el localStorage:", token);
        // Redirigir al usuario a la ubicación deseada
        window.location.href = '/fronted/indexMain';
    })
    .catch((err) => {
        console.log(err);
    });
}

function extractTokenFromUrl(url) {
    const tokenParam = 'token=';
    const startIndex = url.indexOf(tokenParam);
    if (startIndex !== -1) {
        const tokenStartIndex = startIndex + tokenParam.length;
        return url.substring(tokenStartIndex);
    }
    return '';
}

function valuesRegister() {
    const NameUsuario = document.getElementById('Nombre_user').value;
    const RolUsuario = document.getElementById('Rol_user').value;
    const EmailUsuario = document.getElementById('Correo_user').value;
    const PassUsuario = document.getElementById('Contrasena_user').value;

    console.log("Validando Usuarios - Registro|...")
    console.log("Email:",EmailUsuario,"Password:",PassUsuario);

    axios.post('/fronted/saveUsuariosrg',{
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
