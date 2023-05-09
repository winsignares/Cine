function ValuesUser() {
    const Email = document.getElementById('EmailUser').value
    const Password = document.getElementById('PassUser').value

    console.log("getData.Email:'",Email,"'.and.Password:'",Password,"'")

    console.log("Validando User|...")
    axios.post('#rutas/Mainlogin[post](tomarData.tblUser{Email&Password})',{
        /*
        
        */
    })
}