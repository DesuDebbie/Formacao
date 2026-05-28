window.addEventListener("DOMContentLoaded", () => {
    alert("Bem-vindo ao Ikigai by IA | Arte em ganga");
});

const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-image");
const closeBtn = document.querySelector(".close-lightbox");

if (lightbox) {
    document.querySelectorAll(".lightbox-img").forEach(img => {
        img.addEventListener("click", () => {
            lightbox.style.display = "flex";
            lightboxImg.src = img.src;
        });
    });

    closeBtn.addEventListener("click", () => {
        lightbox.style.display = "none";
    });

    lightbox.addEventListener("click", (e) => {
        if (e.target === lightbox) lightbox.style.display = "none";
    });
}

const form = document.getElementById("meuFormulario");
const feedback = document.getElementById("form-feedback");

if (form) {
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const nome = document.getElementById("nome").value.trim();
        const email = document.getElementById("email").value.trim();
        const mensagem = document.getElementById("mensagem").value.trim();

        if (nome === "" || email === "" || mensagem === "") {
            feedback.innerHTML = "<p style='color:#b00020;'>Preenche todos os campos</p>";
        } else {
            feedback.innerHTML = "<p style='color:#4a2c7a;'>Mensagem enviada com sucesso</p>";
            form.reset();
        }
    });
}