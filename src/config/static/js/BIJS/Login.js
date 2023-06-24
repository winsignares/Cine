function valuesUser() {
  const Email = document.getElementById("EmailUser");
  const Password = document.getElementById("PassUser");

  console.log("getData.Email:'", Email, "'.and.Password:'", Password, "'");

  console.log("Validando User|...");
  axios
    .post("/fronted/validarUsuarioslg", {
      email: Email.value,
      password: Password.value,
    })

    .then(function (res) {
      data = res.data;
      window.location.href = res.data.nav;
    })
    .catch((err) => {
      console.log(err);
    });
}
function valuesRegister() {
  const NameUsuario = document.getElementById("Nombre_user").value;
  const RolUsuario = document.getElementById("Rol_user").value;
  const EmailUsuario = document.getElementById("Correo_user").value;
  const PassUsuario = document.getElementById("Contrasena_user").value;

  console.log("Validando Usuarios - Registro|...");
  console.log("Email:", EmailUsuario, "Password:", PassUsuario);

  axios
    .post(
      "/fronted/guardaruser",
      {
        fullname: NameUsuario,
        fullrol: RolUsuario,
        fullcorreo: EmailUsuario,
        fullpassword: PassUsuario,
      },
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    )

    .then((res) => {
      alert("¡REGISTRADO!");
      console.log(res.data);
      window.location.href = "/fronted/indexmainlogin";
    })
    .catch((err) => {
      console.log(err);
    });
}
