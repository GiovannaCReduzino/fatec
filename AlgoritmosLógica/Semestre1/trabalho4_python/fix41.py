#Exercício Fix41 
#Elaborar um algoritmo (programa) que calcule o valor fatorial de um número inteiro positivo. 
#Utilize a estrutura de controle for...in . 
#Cálculo do fatorial, exemplo: fatorial de 5 = 5!=1x2x3x4x5= 120

numero = int (input("\nDigite um número inteiro: ")) 

def calcular_fatorial(numero):
    if numero < 0:
        return "Erro. Número deve ser positivo, maior ou igual a zero"
    
    elif numero ==0:
        return 1
    
    else:
        fatorial = 1
        for i in range (2, numero +1):
            fatorial *= i
        return fatorial

resultado = calcular_fatorial(numero)

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software multiplataformas - 1º semestre Fatec ID")

print (f"\nO fatorial do {numero} é: {resultado}")


