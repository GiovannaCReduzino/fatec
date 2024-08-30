"use strict";
/*Funções no TypeScript
Para rodar, usar: npx tsc (mudar os dados somente no TS)
*/
function calcularArea(lado) {
    return lado * lado;
}
//const quadrado = calcularArea ("b") --> não pode misturar tipos (ex: numer > string). No JS normal "pode"
const quadrado = calcularArea(2); // const quadrado: number = calcularArea(2)
console.log(quadrado);
/*//Para converter
const abc = number (prompt())
const quadrado = calcularArea (b)
console.log(quadrado)
*/
