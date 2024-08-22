#Operadores de Atribuição Simplificada

#Operador > Significado > Exemplo
'''
+= (soma e atribui) 
    x += y 
        #Igual a: x = x + y

-= (subtrai e atribui)
    x -= y 
        #Igual a: x = x - y

*= (multiplica e atribui) 
    x *= y 
        #Igual a: x = x * y

/= (divide e atribui) 
    quociente x /= y 
        #Igual a: x = x / y

**= (exponenciação e atribui) 
    x **= y 
        #Igual a: x = x ** y

//= (quociente da divisão e atribui) 
    x //= y 
        #igual a: x = x // y

%= (divide e atribui resto)
    x %= y 
        #igual a: x = x % y

^= (OU exclusivo e atribui) 
    x ^= y 
        #igual a: x = x ^ y

<<= (desloca à esquerda e atribui) 
    x <<= y 
        #igual x = x<< y

>>= (desloca à direita e atribui)
    x >>= y 
    #igual a: x = x>> y
'''

#Exemplo com Operador:
x = 10; y = 20; x += y - 10
print("x = ",x)

x -= 5
print("x = ",x)

x *= 10
print("x = ",x)

x /= 15
print("x = ",x)