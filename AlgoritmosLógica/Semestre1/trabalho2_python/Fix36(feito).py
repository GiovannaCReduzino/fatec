#Exercício Fix36
#Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível 
#por 10 ou se é divisível por 5 ou se é divisível por 2, caso contrário retornar que o valor não é 
#divisível por nenhum desses valores.

num = int (input("Insira um número inteiro: "))

div_10 = num % 10
div_5 = num % 5
div_2 = num % 2

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021)")

if ((div_10 == 0) & (div_5 == 0) & (div_2 == 0)):
    print("O número", num, "é divisível por 10, 5 e 2")

elif (div_5 == 0):
    print ("O número", num, "é divisível por 5")

elif (div_2 == 0):
    print ("O número", num, "é divisível por 2")

else:
    print ("O número não é divisível por nenhum desses valores")