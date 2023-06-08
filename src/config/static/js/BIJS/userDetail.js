document.addEventListener('DOMContentLoaded',  function () {
    getUserLogged()
})


function getUserLogged() {
  const userId = localStorage.getItem("userId")
  console.log("user logged: ", userId)
  
}
