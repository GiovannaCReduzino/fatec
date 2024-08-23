#Exercício Fix31 
#Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
#(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
#(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; 
#(3) se for os valores 6, 7 e 8, mostre o valor dividido 9.

num = int (input ("Insira um valor inteiro:"))

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021)")

if num in [1, 2, 3]:
    resultado = num **2 #elevado ao quadrado
    print (f"O valor elevado ao quadrado é:", resultado)

elif num in [4, 9]:
    resultado = num **0.5 #raiz quadrada
    print (f"A raiz quadrada do valor é:", resultado)

elif num in [6, 7, 8]:
    resultado = num /9
    print (f"O valor dividido por 9 é: {resultado:.2f}")

else:
    print ("O valor", num, "não possui operações disponíveis.")