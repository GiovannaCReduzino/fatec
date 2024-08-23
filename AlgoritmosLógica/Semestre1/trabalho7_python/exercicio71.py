#Elaborar um programa que determine o cálculo do salário e retorna o valor a ser pago conforme o número de horas trabalhadas. 
#Lembrando que as mesmas serão digitadas.
#Seguem as regras de negócio: Caso a quantidade de horas trabalhadas é menor ou igual a 40, o valor do salário é apenas multiplicando a quantidade de horas pelo valor de cada hora trabalhada. Caso o trabalhar tenha horas extras, é adicionado ao salário um valor pelas horas extras.
#Dica utilizar a função calcular_pagamento (HT, VH)

nome = input ("Digite o nome do funcionário: ")
HT = float (input ("Insira as horas trabalhadas: "))
VH = float (input ("Insira o valor hora: "))
valor_hora_extra = float (input ("Insira o valor pago por hora extra: "))

def calcular_pagamento(HT, VH, valor_hora_extra):

    if HT <=40:
        salario = HT * VH
        horas_extras = 0
    else:
        horas_extras = HT - 40
        salario = (40 * VH) + (horas_extras * valor_hora_extra)
    
    print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
    print ("Desenvolvimento de Software Multiplataformas - 1º semestre Fatec ID")

    print (f"\nTrabalhador: {nome}")
    print (f"Horas trabalhadas: {HT}")    
    print (f"Hora(s) extra(s): {horas_extras}")
    print (f"Seu salário é de: {salario:.2f}")

calcular_pagamento(HT, VH, valor_hora_extra)