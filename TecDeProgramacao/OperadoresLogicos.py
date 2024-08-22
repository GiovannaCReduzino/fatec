#Operadores Lógicos
'''
Certas situações não podem ser modeladas apenas utilizando os operadores aritméticos e/ou relacionais. 
Um exemplo bastante simples disso é saber se uma variável x está dentro de uma faixa de valores. 

Por exemplo, a expressão matemática: 
    0 < 𝑥 < 10 
        (indica que o valor de x deve ser maior do que 0 (zero) e também menor do que 10).
'''

#Operador > Significado > Exemplo
'''
"and" Operador “E” x == 5 and x < y 
    #O resultado é 'True' apenas se ambas as expressões unidas por esse operador também forem.

"or" Operador “OU” x != 5 or x < 0 
    #O resultado é True se alguma das expressões unidas por esse operador também for.

"not" Operador “NEGAÇÃO” not (x > y)
    #inverte o valor lógico da expressão a qual se aplica.
'''

#Exemplo:
x = 5
y = 3
r = (x > 2) and (y < x)
print("Resultado: ",r)
r = (x%2==0) and (y > 0)
print("Resultado: ",r)
r = (x > 2) or (y > x)
print("Resultado: ",r)
r = (x%2==0) or (y < 0)
print("Resultado: ",r)
r = not(x > 2)
print("Resultado: ",r)
r = not(x > 7) and (x > y)
print("Resultado: ",r)
