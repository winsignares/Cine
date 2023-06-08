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
    const user = res.data.user
})
.catch((err) => {
    console.log(err);
})
}
