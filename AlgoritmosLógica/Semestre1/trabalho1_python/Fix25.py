#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
#da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
#que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam 
#R$ 35,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#a) comprar apenas latas de 18 litros;
#b) comprar apenas galões de 3,6 litros;
#c) misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre 
#arredonde os valores para cima, isto é, considere latas cheias.

import math

# Entrada de dados
area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Calcula a quantidade de tinta necessária (com 10% de folga)
tinta_necessaria = area / 6 * 1.1

# Calcula a quantidade e preço de latas
latas = math.ceil(tinta_necessaria / 18)
preco_latas = latas * 80

# Calcula a quantidade e preço de galões
galoes = math.ceil(tinta_necessaria / 3.6)
preco_galoes = galoes * 35

# Calcula a quantidade e preço misturando latas e galões
latas_misturadas = tinta_necessaria // 18
galoes_misturados = math.ceil((tinta_necessaria % 18) / 3.6)
preco_misturado = (latas_misturadas * 80) + (galoes_misturados * 35)

# Quantidade total de litros necessários
litros_total = tinta_necessaria

# Exibe os resultados
print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

print(f"\nQuantidade total de litros necessários: {litros_total:.2f} litros")
print(f"Para comprar apenas latas de 18 litros: {latas} latas. Preço total: R$ {preco_latas:.2f}")
print(f"Para comprar apenas galões de 3,6 litros: {galoes} galões. Preço total: R$ {preco_galoes:.2f}")
print(f"Para misturar latas e galões:\n{int(latas_misturadas)} latas e {galoes_misturados} galões. Preço total: R$ {preco_misturado:.2f}")