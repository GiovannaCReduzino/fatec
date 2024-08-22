print ("Ola, Mundo")

x = 10
print (x)

a = int (input ("Digite o valor de A: "))
b = int (input ("Digite o valor de B: "))

while a <= b: 
    print (a)
    a = a + 1

print ("Fim do programa")

# >Criando um docstring
# = São strings de documetação que fornecem uma explicação que fornecem uma explicação mais detalhada sobre módulos, classes, funções e métodos.
# = Utilizados por 3 aspas (simples ou duplas) 

def soma (a,b):
    '''
    Função para somar dois números.

    Args: 
        a (float): O primeiro número.
        b (float): O segundo número.
    
    Returns:
        float: A soma dos dois números.
    '''
    return a + b 

# >Módulos
# = Os módulos ajudam a evitar a duplicação de código, promovendo a modularidade e a reutilização.
# - Para usar o código de um módulo em outro arquivo Python, você precisa importá-lo
# - Isso é feito usando a palavra-chave import 
import math
import random as rd

#imprime o valor de PI
print (math.pi)

#imprime o valor de RAIZ de 2
print (math.sqrt (2))

#gera um número aleatório entre 0 e 10
print (rd.randint (0,10))

# >Variáveis
'''
= São usadas para armazenar e gerenciar dados, permitindo que você manipule informações de maneira dinâmica
- Você não precisa declarar explicitamente o tipo de uma variável.
- Variáveis definifas fora de qualquer função são chamadas de variáveis globais.
- Letras maiúsculas e minúsculoas são consideradas diferentes.
'''

#Variavel inteira
idade = 25
idade_pessoa = 30

#Variavel de ponto flutuante (float)
altura = 1.75

#Variável de caractere 
letra = 'A'

#Tipos de variáveis
'''
-Inteiro (int): Armazena números inteiros como: 1, -5, 1000
-Número flutuante (float): Armazena números com casas decimais como: 3.14, -0.5, 2.0 
-String (str): Aramzena textos, como: "Olá mundo"
-Booleano (bool): Armazena valores de verdadeiro (true) ou falso (false), usando expressões condicionais.
-Lista (list): Armazena uma coleção ordenada de elementos.
-Tupla (tuple): Similar a uma lista, mas imutável (não pode ser alterada após a criação).
-Dicionário (dict): Armazena pares de chave-valor para mapeamento

-Para saber o tipo da variável, usamos o comando "type(x)"
exemplo:
idade = 25
type(idade)
- Saída - <class 'int'>
'''

#Conversão de tipos
'''
- int(): converte um valor para inteiro via truncagem (apenas a parte inteira é
considerada).
- float(): converte x para em número de ponto flutuante.
- str(): converte um valor em texto (string).
'''

#Print
'''
Para exibir informações na saída padrão (geralmente no console ou terminal), você
pode usar a função print().
Exemplo:
print('Olá, mundo!')
ou 
idade = 25
print ('idade: ', idade)
'''

#Input
'''
Para receber dados do usuário;
Ela permite que o usuário insira dados a partir do teclado
Exemplo:
variável = input()
variável = input(‘texto a ser escrito’)
'''



