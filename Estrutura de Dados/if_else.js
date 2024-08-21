// expressão true
var num = 1;
if (num === 1) {
    console.log('num is equal to 1');
}

// expressão false
var num = 0;
if (num === 1) {
    console.log('num is equal to 1');
} else {
    console.log('num is not equal to 1, the value of num is ' + num);
}

// operação ternário 
if (num === 1) {
    num--;
} else {
    num++;
}

// pode ser escrita --> (num === 1) ? num-- : num++;


// exemplo prático
var month = 5;
if (month === 1) {
    console.log('January');
} else if (month === 2) {
    console.log('February');
} else if (month === 3) {
    console.log('March');
} else {
    console.log('Month is not January, February or March');
}