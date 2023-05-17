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
        alert("Funciono !!")
        window.location.href = res.data

    })

    .catch((err) => {
        console.log(err);
    })
}
function valuesRegister() {
    const EmailUsuario = document.getElementById('InputEmail').value;
    const PassUsuario = document.getElementById('InputPassword').value;

    console.log("Validando Usuarios - Registro|...")
    console.log("Email:",EmailUsuario,"Password:",PassUsuario);

    axios.post('/fronted/validarUsuariosrg',{
        email : EmailUsuario,
        password : PassUsuario
    })
    
    .then((res) => {
        console.log(res.data)
        alert("Funciono !!")
        window.location.href = "/fronted/indexMain"
    })
    .catch((err) => {
        console.log(err);
    })
}