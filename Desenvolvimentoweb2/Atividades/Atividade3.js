function fibonacci(n) {
    if (n === 0) {
        return 0;
    } else if (n === 1) {
        return 1;
    }

    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        let temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

// Exemplo de uso:
let posicao = 10;
console.log(`O número na posição ${posicao} na sequência de Fibonacci é: ${fibonacci(posicao)}`);
