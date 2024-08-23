#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso 
#(p) ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

genero = input ("Insira seu gênero (homem/mulher): ")
altura = float (input ("Insira sua altura: "))

peso_mulheres = (62.1 * altura) - 44.7
peso_homens = (72.7 * altura) - 58

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

if genero == 'mulher':
    print ('\nSeu peso ideal é:', int(peso_mulheres))

elif genero == "homem":
    print ('\nSeu peso ideal é: ', int(peso_homens))

else:
    print ("\nDesculpe, por algum motivo deu erro. Por favor, tente novamente inserindo 'homem' ou 'mulher'.")
