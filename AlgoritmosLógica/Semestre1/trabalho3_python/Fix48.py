def calcular_acrescimo(salario):
    if salario <= 1500:
        acrescimo = salario * 0.20
    elif salario > 1500 and salario < 2500:
        acrescimo = salario * 0.10
    else:
        acrescimo = salario * 0.05
    return acrescimo

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

novo_salario = salario + calcular_acrescimo(salario)

print(f"\n{nome}\nSeu reajuste é de: R$",calcular_acrescimo(salario))
print(f"Seu salário reajustado é: R${novo_salario:.2f}")