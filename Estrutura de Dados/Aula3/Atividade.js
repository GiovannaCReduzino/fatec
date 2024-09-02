/*
Considere uma pilha P vazia e uma fila F não vazia. Utilizando apenas os testes de fila e pilhas vazias
    Operações 'Enfileira', 'Desenfileira', 'Desempilha' e uma variável 'aux' do 'TipoItem'.

Escreva uma função que inverta a ordem dos elementos da fila
 */

function invertaOrdem(fila) {
    let pilha = [];

    // Desenfileira e empilha todos os elementos
    while (fila.length > 0) {
        pilha.push(fila.shift());
    }

    // Desempilha e enfileira os elementos
    while (pilha.length > 0) {
        fila.push(pilha.pop());
    }
}

// Exemplo de uso
let fila = [1, 2, 3, 4, 5];
invertaOrdem(fila);
console.log(fila); // Saída esperada: [5, 4, 3, 2, 1]
