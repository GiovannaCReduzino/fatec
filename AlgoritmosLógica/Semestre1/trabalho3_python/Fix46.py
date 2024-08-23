def modulo(valor):
    return abs(valor)

def diferenca(valor1, valor2):
    return valor1 - valor2

def dividir_por_cinco(valor):
    return valor / 5

valor = float(input("Digite um valor: "))

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

if valor < 0:
    print(f"O módulo do valor é: {modulo(valor):.0f}")

elif valor > 10:
    outro_valor = float(input("Digite outro valor: "))  # Solicita outro valor
    print(f"A diferença entre os valores é: {diferenca(valor, outro_valor):.0f}")

else:
    print(f"O valor dividido por 5 é: {dividir_por_cinco(valor):.1f}")