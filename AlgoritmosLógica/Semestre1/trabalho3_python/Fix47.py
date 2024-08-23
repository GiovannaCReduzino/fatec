def verificar_divisibilidade(numero):
    if numero % 10 == 0 and numero % 5 == 0 and numero % 2 == 0:
        return "é divisível por 10, por 5 e por 2."
    if numero % 10 == 0 and numero % 5 == 0:
        return "é divisível por 10 e por 5."
    if numero % 10 == 0:
        return "é divisível por 10."    
    if numero % 5 == 0:
        return "é divisível por 5."
    if numero % 2 == 0:
        return "é divisível por 2."
    else:
        return "não é divisível por 10, 5, nem por 2."

numero = int(input("Digite um número: "))

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

resultado = verificar_divisibilidade(numero)
    
print(f"\nO número {numero} {resultado}")