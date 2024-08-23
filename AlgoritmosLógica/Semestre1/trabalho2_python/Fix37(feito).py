#Exercício Fix37
#Elabore um programa em Python que o usuário entre com seu e seu salário. Se o salário for 
#menor ou igual a R$1500,00 coloque um acréscimo de 20% de aumento. Se for maior que 
#R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o acréscimo será de 5% 
#para os demais valores.

nome = input ("Insira seu nome:")
salario = float (input("Digite seu salário: R$"))

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021)")

if (salario <=1500.00):
    acrescimo = salario *0.2
    novo_salario = acrescimo + salario
    porcentagem_ganho = 20
    print(f"{nome}, o seu salário atual é de R$ {salario:.2f}.")
    print(f"Valor do aumento: R$ {acrescimo:.2f}")
    print(f"Você receberá um aumento de {porcentagem_ganho}%.")
    print(f"Seu novo salário será de R$ {novo_salario:.2f}.")
  
elif ((salario >1500.00) & (salario <2500.00)):
    acrescimo = salario *0.1
    novo_salario = acrescimo + salario
    porcentagem_ganho = 10
    print(f"{nome}, o seu salário atual é de R$ {salario:.2f}.")
    print(f"Valor do aumento: R$ {acrescimo:.2f}")
    print(f"Você receberá um aumento de {porcentagem_ganho}%.")
    print(f"Seu novo salário será de R$ {novo_salario:.2f}.")

else:
    acrescimo = salario *0.05
    novo_salario = acrescimo + salario
    porcentagem_ganho = 5
    print(f"{nome}, o seu salário atual é de R$ {salario:.2f}.")
    print(f"Valor do aumento: R$ {acrescimo:.2f}")
    print(f"Você receberá um aumento de {porcentagem_ganho}%.")
    print(f"Seu novo salário será de R$ {novo_salario:.2f}.")

