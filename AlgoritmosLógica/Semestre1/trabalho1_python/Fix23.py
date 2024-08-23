#Faça um algoritmo com duas variáveis numéricas (tipo int) que realize as 4 operações básicas 
#(soma, subtração, multiplicação e divisão), mostre os resultados na tela. Os mesmos devem ser 
#solicitados ao usuário, digite os valores via teclado.

a = int(input('Atribua um valor: '))
b = int(input('Atribua outro valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b

'''Evitando divisão com zero (b)'''
if b > 0:
    divisao = a//b
else:
    divisao = "Não é possível dividir por zero"

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

print (f'\nResultado soma: {soma}')
print (f'Resultado subtração: {subtracao}')
print (f'Resultado multiplicação: {multiplicacao}')
print (f'Resultado divisão: {divisao}')