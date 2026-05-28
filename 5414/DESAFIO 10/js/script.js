
window.addEventListener('load', function () {
    alert('Bem-vindo à Ikigai by IA! 🎨✨\n\nExplore os nossos casacos de ganga pintados à mão com temas de anime.');
});

document.addEventListener('DOMContentLoaded', function () {

    const imagemGrande = document.getElementById('imagemGrande');
    const legendaImagem = document.getElementById('legendaImagem');
    const miniaturas = document.querySelectorAll('.miniatura-item');

    miniaturas.forEach(function (miniatura) {
        miniatura.addEventListener('click', function () {
            const novaImagem = this.getAttribute('data-imagem');
            const novaLegenda = this.getAttribute('data-legenda');

            if (novaImagem) {
                imagemGrande.src = novaImagem;
            }

            if (novaLegenda) {
                legendaImagem.textContent = novaLegenda;
            }

            miniaturas.forEach(function (item) {
                item.classList.remove('active');
            });

            this.classList.add('active');
        });

        miniatura.addEventListener('mouseenter', function () {
            const legenda = this.getAttribute('data-legenda');
            if (legenda) {
                this.title = legenda;
            }
        });
    });

    if (miniaturas.length > 0) {
        miniaturas[0].classList.add('active');
    }

    const formNewsletter = document.getElementById('formNewsletter');

    if (formNewsletter) {
        formNewsletter.addEventListener('submit', function (event) {
            event.preventDefault();

            const emailInput = document.getElementById('emailNews');
            const email = emailInput.value.trim();

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (email === '') {
                alert('Por favor, insira o seu endereço de e-mail.');
            } else if (!emailRegex.test(email)) {
                alert('Por favor, insira um endereço de e-mail válido.');
            } else {
                alert('Obrigado por subscrever a nossa newsletter! 📧\nReceberá novidades em breve.');
                emailInput.value = '';
            }
        });
    }

    console.log('Site totalmente funcional! 🌟');
});