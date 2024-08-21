//imprimindo algum valor
console.log('Olá mundo')

//variavel constante, que não pode ser alterada
const a = 10

//variavel mutavel
let b = 20

//tipos primitivos
const c = 10 //number
const d = "teste" //string
const e = true //boolean
const f = null //null
const g = undefined // undefined
const h = Symbol() //Symbol

//operação com as variáveis
const total = a + b
console.log(total)

//If / Else
if(total >30){
    console.log('total > que 30')
} else {
    console.log('total <= 30')
}
//obrigatoriamente, toda linguagem derivada do 'C' tem que usar as chaves para "identar"

//Switch
const dia = "segunda"

switch (dia) {
    case 'segunda':
        console.log('aberto')
        break;
    case 'sábado':
        console.log('fechado')
        break;
    default:
        console.log('meio aberto')
        break;
}

// maneira resumida (para não usar muito if/else)
let idade = 18
let podeBeber = idade >=18 ? 'Pode beber' : 'Não pode'

if (idade >= 18){
    podeBeber = "Pode beber"
} else {
    podeBeber = "Não pode"
}

//Variáveis
const maiorIdade = true
const temCarteiraTrab = false
// && - And / || - Or
const podeAplicarVaga = maiorIdade && temCarteiraTrab

//Operador de negação (!) - fazer depois, me perdi

//Laços de repetição - For
/*for: sabe quantas vezes você quer executar / let: contagem 
/ i <=10:até quando tem que ir /i++: incrementador*/

for (let i = 0; i <= 10; i++) {
    console.log(i)
}

//Laço de repetição - while 

//Laço de repetição - Do While (Faça enquanto)

//Prática
/*Crie um código que vai receber um valor e uma porcentagem de acréscimo 
ao mês, quantos meses são necessários para o valor triplicar? Exiba quantos 
meses levaram para essa condição ocorrer.*/

//commomjs - Importando da biblioteca
//const prompt = require ('prompt-sync')()

import PromptSync from "prompt-sync"
const prompt = PromptSync()

let valor = Number (prompt('Digite o saldo inicial: '))
const percentual = Number (prompt('Digite o percentual desejado: '))
const valorF = valor * 0.3
let meses = 0

while (valor < valorF) {
    valor = valor + percentual
    meses = meses + 1
    console.log(meses)
}