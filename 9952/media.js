const notas = []
let nota

while (true) {
    nota = prompt("Introduza uma nota (ou escreva FIM para terminar):")

    if (nota.toUpperCase() === "FIM") {
        break
    }

    nota = parseInt(nota)
    notas.push(nota)
}

if (notas.length > 0) {
    let soma = 0
    for (let nota of notas) {
        soma += nota
    }
    const media = soma / notas.length
    console.log("Média:", media)
} else {
    console.log("Lista de números vazia! Não posso calcular a média...")
}