valor = int(input("Digite um valor: "))

def calcular_cubo(valor):
    return valor ** 3

def calcular_fatorial(valor):
    if valor == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, valor + 1):
            fatorial *= i
        return fatorial

def dividir_por_nove(valor):
    return valor / 9

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

if (valor == 1) or (valor == 2):
    print(f"\nO valor {valor} elevado ao cubo é {calcular_cubo(valor):.0f}.")
elif (valor % 3 == 0):
    print(f"\nO fatorial de {valor} é {calcular_fatorial(valor):.0f}.")
elif ((valor == 4) or (valor == 5) or (valor == 7) or (valor ==8)):
    print(f"\nO valor {valor} dividido por 9 é {dividir_por_nove(valor):.2f}.")
else:
    print("Valor inválido.")