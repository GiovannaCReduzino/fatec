#Operadores Relacionais
'''
São aqueles que operam sobre dois valores (valores, variáveis ou chamadas de funções) 
e/ou expressões aritméticas e verificam a magnitude (quem é maior ou menor) 
e/ou igualdade entre eles. 
'''

#Operador > Significado > Exemplo
'''
> Maior do que x > 5
>= Maior ou igual a x >= 10
< Menor do que x < 5
<= Menor ou igual a x <= 10
== Igual a x == 0
!= Diferente de x != 0
'''

'''
Como resultado, esse tipo de operador retorna:
    O valor True, se a expressão relacional for considerada verdadeira;
    O valor False, se a expressão relacional for considerada falsa.
'''

#Exemplo:
x = 5
y = 3
print("Expressão 1: ",x > 4) #Expressão 1: True
print("Expressão 2: ",x == 4) # Expressão 2: False
print("Expressão 3: ",x != y) # Expressão 3: True
print("Expressão 4: ",x != y+2) # Expressão 4: False

