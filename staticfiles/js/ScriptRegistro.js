function redirigirACorreo(correoUsuario) {
    let dominio = correoUsuario.split("@")[1];
    let enlace;

    if (dominio === "gmail.com") {
        enlace = "https://mail.google.com/";
    } else if (dominio === "outlook.com" || dominio === "hotmail.com") {
        enlace = "https://outlook.live.com/";
    } else if (dominio === "yahoo.com") {
        enlace = "https://mail.yahoo.com/";
    } else {
        enlace = "https://www." + dominio;
    }

    return enlace;
}

//Uso en SweetAlert
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get("registro_exitoso") === "1") {
    Swal.fire({
        title: "¡Registro exitoso!",
        text: "Hemos enviado un enlace de confirmación a tu correo. Por favor revisa tu bandeja.",
        icon: "success",
        confirmButtonText: "Abrir mi correo",
        showCancelButton: true,
        cancelButtonText: "Cerrar",
        confirmButtonColor: "#00D084",
        cancelButtonColor: "#d33",
    }).then((result) => {
        if (result.isConfirmed) {
            window.open("https://mail.google.com/", "_blank"); // Cambia según el dominio
        }
    });
}


function alertaRecuperacion(correoUsuario) {
    const enlaceCorreo = redirigirACorreo(correoUsuario);
    Swal.fire({
        title: "coreo enviado ",
        text: "El enlace para recuperar tu contraseña fue enviado a tu correo. Revisa tu bandeja y sigue los pasos para crear una nueva contraseña.",
        icon: "success",
        confirmButtonText: "Abrir mi correo",
        showCancelButton: true,
        cancelButtonText: "Cerrar",
        confirmButtonColor: "#00D084",
        cancelButtonColor: "#d33",
    }).then((result) => {
        if (result.isConfirmed) {
            window.open(enlaceCorreo, "_blank");
        }
    });
}