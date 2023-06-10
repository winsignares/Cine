document.addEventListener('DOMContentLoaded',  function () {
    getUserLogged()
})


function getUserLogged() {
  const userId = localStorage.getItem("userId")
  console.log("user logged: ", userId)
  axios.post('/fronted/getuser', {
    userid: userId
  })

.then(function(res){ 
    const user = res.data.name
    const nameUser = document.getElementById("Update-nameUser")
    nameUser.innerHTML = `
    <span id="Update-nameUser" class="user-name" onclick="toggleDropdown()">${user}</span>
    `
})
.catch((err) => {
    console.log(err);
})
}
