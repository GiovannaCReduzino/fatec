/* Instalações:

- Para baixar o prompt-sync: "npm i prompt-sync"
- Para instalar a dependencia de desenvolvimento a tipagem de prompt-sync: "npm i -D @types/prompt-sync"
*/

import PromptSync from 'prompt-sync'
const prompt = PromptSync()

/*Funções no TypeScript 
Para rodar, usar: npx tsc (mudar os dados somente no TS)
*/
function calcularArea (lado: number): number{ //tem que colocar a tipagem depois dos ":" (sempre tem que colocar o tipo da variável)
    return lado *lado
}

//const quadrado = calcularArea ("b") --> não pode misturar tipos (ex: numer > string). No JS normal "pode"
const quadrado = calcularArea (2) // const quadrado: number = calcularArea(2)
console.log(quadrado)

/* > Para converter tipos
const abc = number (prompt())
const quadrado = calcularArea (b)
console.log(quadrado)
*/

/* > Let:
let texto: string " "
*Impossível mudar uma variável
let texto = ""
texto = "10"
*/

/* > Interfaces:

São formas de definir contratos ou estruturas para objetos
    "Força" a pessoa a não errar
(Para sempre chamar fora da chave, eu preciso que a "info" esteja dentro do const)

*/

type situacao = 'Aprovado' | 'reprovado' //para travar status que não podem ser mudados durante o código

interface Aluno { // ou "type Aluno = "
    nome: string
    mediaFinal: number
    situacao: string
}

const aluno: Aluno = {
    nome: "", //string
    mediaFinal: 9, //number
    situacao: "Aprovado" //string
}

const aluno2: Aluno = {
    nome: "Teste 2",
    mediaFinal: 9,
    situacao: "Aprovado"
}

/*Usando Function*/
function alunoFactory (nome: string, mediaFinal: number){
    
    let situacao: situacao
    if (mediaFinal > 6){
        situacao = 'Aprovado'
    } else {
        situacao = 'reprovado'
    }

}

console.log (aluno.nome) //Acessando tributos ou métodos (função) do objeto

/* > Para "matar" o 'else' (ficar mais bonito o código): 

function alunoFactory (nome: string, mediaFinal: number){
    
    let situacao: situaao = 'reprovado'
    if (mediaFinal > 6){
        situacao = 'Aprovado' 
    }

    return { //se tem o mesmo nome na variável, pode puxar sem os valores
        nome: nome,
        mediaFinal,
        situacao
    }

}

const aluno3 = alunoFactory ('Teste 3', 9)
console.log (aluno3.situacao)
*/



