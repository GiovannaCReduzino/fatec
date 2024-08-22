#Operadores aritméticos
'''
São aqueles que operam sobre valores numéricos (valores, variáveis ou chamadas de funções) 
e/ou expressões e tem como resultado valores numéricos.
'''

#Operador > Significado > Exemplo
'''
+ adição de dois valores (z = x + y)
- subtração de dois valores (z = x - y)
* multiplicação de dois valores (z = x * y)
/ quociente de dois valores (z = x / y)
** exponenciação de dois valores (z = x ** y)
// Quociente da divisão inteira (z = x // y)
% resto de uma divisão inteira (z = x % y)
'''

#Exemplo:
x = 10; y = 20; z = x * y
print("z = ",z)

z = y/10
print("z = ",z)
print("x+y = ",x+y)

'''
Em uma expressão, as operações de exponenciação, multiplicação,
divisão, e resto são executados antes das operações de adição e subtração. 
Para forçar uma operação a ser executada antes das demais, colocamos ela entre (parênteses)

Exemplo:

z = x * y + 10 #Saída = 210

z = x * (y + 10) #Saída = 300
'''

