valor = int(input("Digite um valor de 1 à 9, exceto 5: "))

import math

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

if valor in [1, 2, 3]:
    print(f"\n{valor} elevado ao quadrado é {valor ** 2}.")
elif valor in [4, 9]:
    print(f"\nA raiz quadrada de {valor} é {math.sqrt(valor)}")
elif valor in [6, 7, 8]:
    print(f"\n{valor} dividido por 9 é {valor/9:.2f}.")
else:
    print("\nValor fora do intervalo válido (1 à 9, exceto 5).")
