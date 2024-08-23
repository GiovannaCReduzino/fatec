#Exercício Fix32 
#Faça um algoritmo que calcule a média do aluno. Ele deve entrar com seu nome, ra, nota 1 e 
#nota 2. O sistema deverá informar a ele as seguintes mensagens:
#a) Se a média for maior ou igual a sete: Parabéns, você está aprovado!
#b) Se a média for menor que sete: Você ainda tem uma chance! Estude mais para o exame.

nome = input ("Digite seu nome: ")
ra = int (input ("Insira o RA do aluno: "))
nota1 = float (input("Insira a nota1: "))
nota2 = float (input("Insira a nota2: "))

media = (nota1 + nota2) //2

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021)")

if media >= 7:
    print ("Parabéns, você está aprovado!")

else:
    print ("Você ainda tem uma chance! Estude mais para o exame.")