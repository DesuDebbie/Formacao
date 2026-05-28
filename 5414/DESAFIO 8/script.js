function mediaEscolar() {
    let nota1 = parseFloat(prompt("Primeira nota:"));
    let nota2 = parseFloat(prompt("Segunda nota:"));
    let nota3 = parseFloat(prompt("Terceira nota:"));
    let nota4 = parseFloat(prompt("Quarta nota:"));

    if (isNaN(nota1) || isNaN(nota2) || isNaN(nota3) || isNaN(nota4)) {
        document.getElementById("resMedia").innerHTML = "Aviso: Tens de meter numeros validos";
        return;
    }

    let media = (nota1 + nota2 + nota3 + nota4) / 4;

    let situacao = "";
    if (media >= 9.5) {
        situacao = "APROVADO";
    } else {
        situacao = "REPROVADO";
    }

    document.getElementById("resMedia").innerHTML =
        "Notas: " + nota1 + ", " + nota2 + ", " + nota3 + ", " + nota4 + "<br>" +
        "Media: " + media.toFixed(2) + "<br>" +
        "Situacao: " + situacao;
}

function circulo() {
    let raio = parseFloat(prompt("Qual e o raio do circulo?"));

    if (isNaN(raio) || raio <= 0) {
        document.getElementById("resCirculo").innerHTML = "Aviso: Raio invalido. Mete um numero positivo.";
        return;
    }

    let perimetro = 2 * Math.PI * raio;
    let area = Math.PI * raio * raio;

    document.getElementById("resCirculo").innerHTML =
        "Raio: " + raio + "<br>" +
        "Perimetro: " + perimetro.toFixed(2) + "<br>" +
        "Area do circulo: " + area.toFixed(2);
}

function operacoes() {
    let numA = parseFloat(prompt("Digite o primeiro numero:"));
    let numB = parseFloat(prompt("Digite o segundo numero:"));

    if (isNaN(numA) || isNaN(numB)) {
        document.getElementById("resOperacoes").innerHTML = "Aviso: Isso nao e um numero valido";
        return;
    }

    let soma = numA + numB;
    let subtracao = numA - numB;
    let multiplicacao = numA * numB;

    let divisao;
    if (numB === 0) {
        divisao = "ERRO - Nao podes dividir por zero";
    } else {
        divisao = numA / numB;
    }

    document.getElementById("resOperacoes").innerHTML =
        "Numeros: " + numA + " e " + numB + "<br>" +
        "Soma: " + soma + "<br>" +
        "Subtracao: " + subtracao + "<br>" +
        "Multiplicacao: " + multiplicacao + "<br>" +
        "Divisao: " + divisao;
}