function validar() {
    var telemovel = document.formulario.telemovel.value;

    if (isNaN(telemovel)) {
        alert("O número de telemóvel não está correto.");
        return false;
    }

    if (telemovel.length != 9) {
        alert("O número de telemóvel deve ter 9 dígitos.");
        return false;
    }

    if (!telemovel.startsWith('9')) {
        alert("Telemóvel tem de começar por 9.");
        return false;
    }

    var email = document.formulario.email.value;
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!re.test(String(email).toLowerCase())) {
        alert("Email inválido");
        return false;
    }

    alert("Obrigado! Entraremos em contacto brevemente para falar do seu casaco personalizado.");
    return true;
}