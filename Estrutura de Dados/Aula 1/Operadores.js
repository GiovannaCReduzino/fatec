// operadores aritméticos
var num = 0; 
num = num + 2;
num = num * 3;
num = num / 2;
num = num % 2
num++; // incremento
num--; // decremento

// operadores de atribuição
// atribuição referente ao sinal 
num += 1;    
num -= 2;
num *= 3;
num /= 2;
num %= 3;

// operadores de comparação
console.log('num == 1 : ' + (num == 1)); // igual a 
console.log('num === 1 : ' + (num === 1)); // igual em valor e tipo
console.log('num != 1 : ' + (num != 1)); // diferente
console.log('num > 1 : ' + (num > 1)); // maior
console.log('num < 1 : ' + (num < 1)); // menor
console.log('num >= 1 : ' + (num >= 1)); // maior igual
console.log('num <= 1 : ' + (num <= 1)); // menor igual

// operadores lógicos
console.log('true && false : ' + (true && false)); // E
console.log('true || false : ' + (true || false)); // OU
console.log('!true : ' + (!true)); // Negação

// Typeof = saber o tipo da variável
console.log('typeof num:', typeof num);

var myObj = {nome: 'John', idade: 21}; // criou um array com nome e idade
delete myObj.idade; // deletou o objeto idade 
console.log(myObj); 