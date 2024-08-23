/*Crie um código com Node que escreva a tabuada de um número digitado pelo usuário.
A tabuada deve ser apresentada no console como:
1X2=2
2X2=4*/

import PromptSync from "prompt-sync"
const prompt = PromptSync ()

let num = Number (prompt('Digite o número que você quer multiplicar: '))
let tabuada = 0

for (let i = 1; i <=10; i++){
    tabuada = num * i
    console.log(`${i}X${num}=${tabuada}`)
}