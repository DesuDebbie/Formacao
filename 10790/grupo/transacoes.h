#include <stdio.h>      // Biblioteca para funções de ecrã (printf)
#include <string.h>     // Biblioteca para manipular texto (strcpy)
#include "transacoes.h" // Ficheiro com as estruturas Pilha e Conta

/* C23: nullptr é um ponteiro real e puro. Mais seguro que o NULL antigo. */
void inicializarPilha(Pilha *p) // Prepara a pilha
{
    if (p != nullptr) // Se a pilha existir na memória
    {
        p->top = -1; // Define o topo em -1 (pilha vazia)
    }
}

bool estaCheia(Pilha *p) // Verifica se a pilha encheu
{
    // Retorna verdadeiro se o topo chegou à última posição (9)
    return p != nullptr && p->top == SIZE - 1;
}

bool estaVazia(Pilha *p) // Verifica se a pilha está sem dados
{
    // Retorna verdadeiro se o topo for -1 ou o ponteiro for nulo
    return p == nullptr || p->top == -1;
}

void push(Pilha *p, char descricao[], float v) // Insere dados na pilha
{
    if (p == nullptr || estaCheia(p)) // Proteção: se for nula ou cheia
        return;                       // Aborta e sai da função

    p->top++;                                 // Sobe o topo para a próxima posição livre
    strcpy(p->itens[p->top].acao, descricao); // Guarda o nome do movimento
    p->itens[p->top].valor = v;               // Guarda o valor do movimento
}

void mostrarHistorico(Pilha *p) // Mostra o extrato no ecrã
{
    if (p == nullptr || estaVazia(p)) // Se não existirem movimentos
    {
        printf("\nSem movimentos.\n"); // Avisa o utilizador
        return;                        // Sai da função
    }
    printf("\n--- HISTORICO ---\n");

    // LIFO: O ciclo começa no topo e desce até ao zero (último entra, primeiro sai)
    for (int i = p->top; i >= 0; i--)
    {
        printf("%s: %.2f EUR\n", p->itens[i].acao, p->itens[i].valor); // Imprime a linha
    }
}

bool levantar(Conta *c, float valor, Pilha *p) // Função de levantamento
{
    // Valida se a conta existe, se o valor é positivo e se há saldo suficiente
    if (c == nullptr || valor <= 0 || c->saldo < valor)
        return false; // Se falhar alguma, cancela a operação e retorna falso

    c->saldo -= valor;               // Subtrai o valor ao saldo atual na RAM
    push(p, "Levantamento", -valor); // Guarda a operação na pilha com valor negativo
    return true;                     // Retorna verdadeiro (sucesso)
}

void depositar(Conta *c, float valor, Pilha *p) // Função de depósito
{
    if (c == nullptr || valor <= 0) // Valida conta e se o valor é positivo
        return;                     // Se falhar, sai da função

    c->saldo += valor;          // Soma o valor ao saldo atual na RAM
    push(p, "Deposito", valor); // Guarda a operação na pilha com valor positivo
}

bool transferir(Conta *origem, Conta *destino, float valor, Pilha *p) // Função de transferência
{
    // Valida as duas contas, o valor positivo e se a origem tem saldo suficiente
    if (origem == nullptr || destino == nullptr || valor <= 0 || origem->saldo < valor)
    {
        return false; // Se falhar alguma, cancela tudo e retorna falso
    }

    origem->saldo -= valor;           // Retira o dinheiro à conta de origem
    destino->saldo += valor;          // Adiciona o dinheiro à conta de destino
    push(p, "Transferencia", -valor); // Guarda o movimento de débito na pilha
    return true;                      // Retorna verdadeiro (sucesso)
}