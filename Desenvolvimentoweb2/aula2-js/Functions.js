/*
Function: É onde a função é definida e nomeada
Parâmetros: são as variáveis que a função recebe como entrada
Corpo da função: Bloco do código que contém as instruções executadas quando a função é chamadas (o que está entre chaves {})
Return: Valor que a função retorna após executar 
*/

function somar(a,b){ /*(a,b): Parâmetros da função*/
    const total = a + b
    return Number(total) /*Number: Força o resultado ser um número*/
}

function calcular (a, b, operacao){
    const resultado = operacao (a,b)
    console.log (resultado)
    return resultado 
}
console.log (50) /*Calcular a = 20 e b = 30 e operacao = fn somar() | Somar a = 20 e b = 30 e total = 50*/

function imprimir (texto){
    console.log(texto) /*Undefined (Void) - não pode voltar como variável*/ /*Local*/
}

const teste = somar (10,20) /*Valores dos parâmetros*/
imprimir (texto) /*Global*/

//Atalho de funções
/*

*/

const atalho = console.log /*Atribui o valor de função para a variável*/
const atalho2 = somar

function calcular (a, b, operacao){
    return operacao (a,b) //Operação: somar
}

calcular (20, 30, somar)

//Arrow function (=>)
/* 

obs: Ambos (const e function) fazem o mesmo
*/

const sub = (a, b) => { /*aqui está em uma constante - como se fosse uma função anônima*/ /* */
    return a - b
}

/*function sub2 (a,b){ //aqui está em uma função - se usar essa na hora de chamar, o código será maior
    return a - b
}*/

/*Calcular (30, 20, function sub(a,b){ ((aqui está chamando caso crie função))
    //
})
*/

/*Chamando uma Arrow Function */
calcular (30, 20, (a,b) => { /*Calcular (30, 20, (a,b) =>) */
    //
})

/*O arrow function pode fazer sem o return e sem parâmetros*/

