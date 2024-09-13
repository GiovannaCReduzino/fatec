import promptSync from "prompt-sync"
const prompt = promptSync()

let valorCelcius = Number(prompt('Digite um número: '))

function converterFahrenheit(valorCelcius) {
    return (valorCelcius * 9 / 5) + 32
}
console.log(converterFahrenheit(valorCelcius))