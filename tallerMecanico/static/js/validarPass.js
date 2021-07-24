let pass1 = document.getElementById("txtPass1").value;
let pass2 = document.getElementById("txtPass2").value;
if (pass1 != pass2) {
    alert("Las contraseñas no coinciden");
    return false;
}
return true;

