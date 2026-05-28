#include <stdio.h>
#include <string.h>
#include "transacoes.h"

/* NOTA C23: O nullptr substitui o NULL antigo por ser um ponteiro real e seguro */
void inicializarPilha(Pilha *p)
{
    if (p != nullptr) // Se a estrutura da pilha existir na memória...
    {
        p->top = -1; // ...define o topo como -1 (significa que está vazia).
    }
}
/* a PILHA UTILIza a logica de LIFO, basicamente quando o utilizador ve o historico de movimentacoes, aparece primeiro a ultima movimentacao feita, e depois as anteriores, ou seja,
 a ultima movimentacao fica no topo da pilha, e as anteriores ficam abaixo dela.*/

{
    // Retorna verdadeiro se a pilha existir e o topo chegar à última posição (9)
    return p != nullptr && p->top == SIZE - 1;
}

bool estaVazia(Pilha *p)
{
    // Retorna verdadeiro se a pilha não existir ou se o topo ainda for -1
    return p == nullptr || p->top == -1;
}

void push(Pilha *p, char descricao[], float v)
{
    if (p == nullptr || estaCheia(p)) // Se a pilha for inválida ou estiver cheia...
        return;                       // ...para imediatamente a função e ignora o registo.

    p->top++;                                 // Sobe o indicador do topo para a próxima posição livre.
    strcpy(p->itens[p->top].acao, descricao); // Copia o nome da ação para o registo atual.
    p->itens[p->top].valor = v;               // Guarda o valor ganho ou gasto no registo atual.
}

void mostrarHistorico(Pilha *p)
{
    if (p == nullptr || estaVazia(p)) // Se não houver pilha ou se estiver vazia...
    {
        printf("\nSem movimentos.\n"); // ...avisa o utilizador no ecrã...
        return;                        // ...e sai da função.
    }
    printf("\n--- HISTORICO ---\n"); // Imprime o cabeçalho do extrato.

    // LIFO: Começa no último elemento guardado (top) e desce até ao primeiro (0)
    for (int i = p->top; i >= 0; i--)
    {
        // Mostra o texto e o valor de cada movimento guardado na pilha
        printf("%s: %.2f EUR\n", p->itens[i].acao, p->itens[i].valor);
    }
}

bool levantar(Conta *c, float valor, Pilha *p)
{
    // Valida se a conta existe, se o valor é maior que zero e se há saldo suficiente
    if (c == nullptr || valor <= 0 || c->saldo < valor)
        return false; // Se alguma falhar, recusa o levantamento e devolve falso.

    c->saldo -= valor;               // Retira o dinheiro diretamente ao saldo da conta na RAM.
    push(p, "Levantamento", -valor); // Insere a operação no histórico com valor negativo.
    return true;                     // Devolve verdadeiro para confirmar o sucesso.
}

void depositar(Conta *c, float valor, Pilha *p)
{
    if (c == nullptr || valor <= 0) // Se a conta for inválida ou o valor for zero/negativo...
        return;                     // ...ignora e sai da função.

    c->saldo += valor;          // Adiciona o dinheiro diretamente ao saldo da conta na RAM.
    push(p, "Deposito", valor); // Insere o registo do depósito na pilha de sessão.
}

bool transferir(Conta *origem, Conta *destino, float valor, Pilha *p)
{
    // Valida as duas contas, o valor positivo e se quem envia tem dinheiro suficiente
    if (origem == nullptr || destino == nullptr || valor <= 0 || origem->saldo < valor)
    {
        return false; // Se algo falhar, cancela tudo e devolve falso.
    }

    origem->saldo -= valor;           // Retira o dinheiro à conta de quem envia.
    destino->saldo += valor;          // Adiciona o dinheiro à conta de quem recebe.
    push(p, "Transferencia", -valor); // Regista a transferência como um débito na pilha.
    return true;                      // Devolve verdadeiro para confirmar o sucesso da transferência.
}