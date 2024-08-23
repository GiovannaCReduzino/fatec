#Exercício Fix40
#Elabore um programa em Python que o usuário entre com seu e seu salário. 
#Se o salário for menor ou igual a R$1500,00 coloque um acréscimo de 20% de aumento. 
#Se  for  maior  que  R$1500,00 e  menor  que  R$2500,00  o  acréscimo  será  de  10%.  
#Senão  o acréscimo será de 5% para os demais valores.

nome = input ("\nInsira seu nome: ")
salario = float (input ("Por favor, digite seu salário: R$ "))

def calcular_acrescimo(salario):
    if (salario <= 1500):
        acrescimo = salario * 0.2
        porcentagem_ganho = 20

    elif (1500 < salario <= 2500):
        acrescimo = salario *0.1
        porcentagem_ganho = 10

    else:
        acrescimo = salario *0.05
        porcentagem_ganho = 5
        
    return acrescimo, porcentagem_ganho 

acrescimo, porcentagem_ganho = calcular_acrescimo(salario)

novo_salario = salario + acrescimo

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software multiplataformas - 1º semestre Fatec ID")

print (f"\n{nome}, seu acrescimo foi de: {porcentagem_ganho}%")
print (f"Seu novo salário é de: R${novo_salario:.2f}")