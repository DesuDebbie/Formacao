#include <stdio.h> // Biblioteca para usar o printf
#include "transacoes.h" // Ficheiro com as estruturas da Conta e da Pilha

int main() // Função principal onde o teste começa a ser executado
{
    // Cria uma conta fictícia na RAM com dados de teste e 500€ de saldo
    Conta contaTeste = {
        .numero_conta = 1001,
        .nome = "Conta Teste",
        .pin_encriptado = 0,
        .saldo = 500.00,
        .next = -1,
        .is_supervisor = false};

    Pilha historico; // Cria uma variável para guardar o histórico da sessão
    inicializarPilha(&historico); // Prepara a pilha (coloca o topo em -1)

    printf("--- TESTE MODULO 2 ---\n");
    printf("Saldo Inicial: %.2f EUR\n", contaTeste.saldo); // Mostra os 500€ iniciais

    // Passa a conta e a pilha por referência (&) para retirar 100€
    levantar(&contaTeste, 100.00, &historico);
    printf("Apos levantar 100 EUR: %.2f EUR\n", contaTeste.saldo); // Mostra o novo saldo (400€)

    // Passa a conta e a pilha por referência (&) para depositar 50€
    depositar(&contaTeste, 50.00, &historico);
    printf("Apos depositar 50 EUR: %.2f EUR\n", contaTeste.saldo); // Mostra o novo saldo (450€)

    // Imprime o extrato final (mostra o Depósito primeiro devido ao LIFO)
    mostrarHistorico(&historico);

    return 0; // Termina o programa de teste com sucesso
}