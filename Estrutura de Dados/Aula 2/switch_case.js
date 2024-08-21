// e determina se o valor de switch é igual ao valor da cláusula case.
var month = 5;
switch (month) {
    case 1:
        console.log('January');
        break;
    case 2:
        console.log('February');
        break;
    case 3:
        console.log('March');
        break; // para o laço
    default: // é executado caso nenhuma das instruções do case seja true
        console.log('Month is not January, February or March');
}