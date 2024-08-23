'''estrutura If'''

#num = int(input("Digite um número: "))
#if(num > 0):
#print("O número digitado é maior do que 0", num)

'''estrutura Else'''
#num = int(input("Digite um número: "))
#else:
#print("O número digitado = "+ str(num) +" é menor do que 0")

''' Exemplo If - Else '''

#num = int(input("Digite um número: "))
#if(num > 0):
    #print("O número digitado = "+ str(num) +" é maior do que 0")
#else:
    #print("O número digitado = "+ str(num) +" é menor do que 0")

'''Exemplo (2): Determine se o número digitado pelo usuário é par ou ímpar. Dica, utilize a estrutura de desvio condicional 
(if...else)'''

#num = int(input("Digite um número : "))
#'''print("Programa que determina se o numero digitado é par ou impar")'''
#if(not num % 2):
 #print("O número digitado é par." ,num)
#else:
 #print("O número digitado é ímpar." ,num)

''' Estrutura Elif
Exemplo: Determinar se pode votar'''

idade = int(input("Informe a sua idade: "))
if(idade<=0):
 print("A sua idade não pode ser 0 ou menor do que 0!" , idade)
elif (idade>120):
 print("A sua idade não pode ser superior a 120 ano!", idade)
elif (idade>=16) and (idade<120):
 print("Parabens, vc pode votar!", idade)
else:
 print("Você precisa ter mais do que 18 anos!", idade)

 