""" Dados dois conjuntos contendo 5 elementos ,cada conjunto. 
OBS: o conjunto (vetor) não deve conter elementos repetidos, para isso implemente o carregamento do vetor contendo elementos não repetidos. 

Calcule a união, intersecção, A-B, B-A, diferença simétrica e P(A). 
Apresentar os conjuntos A e B de forma classificada crescentemente. 
Para as operações acima, não apresente elemento repetido. 
Apresente a palavra VAZIO para quando o vetor de respostas não tiver elemento. """

# Bloco de importação
from itertools import chain, combinations

# Variáveis
nomeA = "conjuntoA"
nomeB = "conjuntoB"

# Bloco de criação do conjunto A
vetorA = []
print(f"\n--> Digite 5 elementos para o {nomeA}: ")
while len(vetorA) < 5:
    elemento = int(input(f"\nElemento {len(vetorA) + 1}: "))
    if elemento not in vetorA:
        vetorA.append(elemento)
    else:
        print("\nElemento repetido, insira outro.")
conjunto_a = sorted(vetorA)

# Bloco de criação do conjunto B
vetorB = []
print(f"\n--> Digite 5 elementos para o {nomeB}: ")
while len(vetorB) < 5:
    elemento = int(input(f"\nElemento {len(vetorB) + 1}: "))
    if elemento not in vetorB:
        vetorB.append(elemento)
    else:
        print("\nElemento repetido, insira outro.")
conjunto_b = sorted(vetorB)

# Bloco de união
uniao_result = sorted(list(set(conjunto_a) | set(conjunto_b)))

# Bloco de intersecção
intersecao_result = sorted(list(set(conjunto_a) & set(conjunto_b)))

# Bloco de diferença A - B
a_menos_b_result = sorted(list(set(conjunto_a) - set(conjunto_b)))

# Bloco de diferença B - A
b_menos_a_result = sorted(list(set(conjunto_b) - set(conjunto_a)))

# Bloco de diferença simétrica
diferenca_simetrica_result = sorted(list(set(conjunto_a) ^ set(conjunto_b)))

# Bloco de partes do conjunto A
partes_a_result = list(chain.from_iterable(combinations(conjunto_a, r) for r in range(len(conjunto_a) + 1)))

# Bloco de impressão

print (f"\n--> Resposta: ")
if conjunto_a:
    print(f"\nConjunto A: {conjunto_a}")
else:
    print(f"\nConjunto A: VAZIO")

if conjunto_b:
    print(f"\nConjunto B: {conjunto_b}")
else:
    print(f"\nConjunto B: VAZIO")

if uniao_result:
    print(f"\nA ∪ B: {uniao_result}")
else:
    print(f"\nA ∪ B: VAZIO")

if intersecao_result:
    print(f"\nA ∩ B: {intersecao_result}")
else:
    print(f"\nA ∩ B: VAZIO")

if a_menos_b_result:
    print(f"\nA - B: {a_menos_b_result}")
else:
    print(f"\nA - B: VAZIO")

if b_menos_a_result:
    print(f"\nB - A: {b_menos_a_result}")
else:
    print(f"\nB - A: VAZIO")

if diferenca_simetrica_result:
    print(f"\nA ∆ B: {diferenca_simetrica_result}")
else:
    print(f"\nA ∆ B: VAZIO")

print(f"\nP(A): {partes_a_result}")

