//Sintaxe básica de uma função. Sem argumentos e nem a instrução "return"
function sayHelo (){
    console.log('Hello!')
}

//Argumentos
// - Argumentos são variáveis com as quais se supõe que a função fará algo
output('Hello')
//Pode usar quantos argumentos quiser, assim: (mas, neste caso, apenas o primeiro argumento será usado pela função; o segundo será ignorado)
output ('Hello', 'Other text')

//Uma função também pode devolver um valor:
function sum (num1, num2) {
    return num1 + num2;
}
//-Essa função calcula a soma de dois números especificados e devolve o resultado. Podemos usá-la daa seguinte maneira:
var result = sum (1,2);
output (result) //a saída é 3