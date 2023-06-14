// Obtener el token desde el almacenamiento local (localStorage)
function getTokenFromLocalStorage() {
    const token = localStorage.getItem('token');
    return token;
}
