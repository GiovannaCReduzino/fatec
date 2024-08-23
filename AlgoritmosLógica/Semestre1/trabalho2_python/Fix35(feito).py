#Exercício Fix35
#Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
#(1) se for um valor negativo, mostre o módulo (valor sem sinal) do valor;
#(2) se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;
#(3) Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5


valor = float(input("Digite um valor: "))

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021)")

if valor < 0:
    valor_modulo = abs(valor)  # Módulo do valor (sem sinal)
    print(f"O módulo do valor é: {valor_modulo}")
elif valor > 10:
    novo_valor = float(input("Digite outro valor: "))
    diferenca = valor - novo_valor
    print(f"A diferença entre os valores é: {diferenca}")
else:
    resultado = valor / 5
    print(f"O valor dividido por 5 é: {resultado}")


#abs: A função abs() em Python é uma função embutida que retorna o valor absoluto de um número. 
#Em termos simples, ela retorna o valor numérico sem o sinal.
#Por exemplo:
#abs(5) retorna 5
#abs(-5) também retorna 5
#A função abs() é útil quando você precisa garantir que um número seja sempre positivo, 
#independentemente do sinal que ele tenha. 
#No contexto do programa fornecido anteriormente, a função abs() foi utilizada para calcular o módulo (valor sem sinal) 
#de um número negativo.