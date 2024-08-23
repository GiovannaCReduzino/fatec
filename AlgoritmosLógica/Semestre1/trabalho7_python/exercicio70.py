#Desenvolva um programa para determinar a média geral do aluno. O mesmo deverá receber o nome do aluno, as 2 notas obtidas do aluno nas 2 avaliações. 
#Calcular a média de aproveitamento, usando a fórmula da Media e escrever o conceito do aluno de acordo com a tabela de conceitos.
#Média é dada pela fórmula: MG = (NP1*4 + NP2*6) / 10 
#Incluir uma mensagem a qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois faça um(printscreen) e comentar o(s) resultado(s) do programa após a execução do mesmo.

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da NP1: "))
nota2 = float(input("Digite a nota da NP2: "))

def calcular_e_mostrar_resultado():

    media = (nota1 * 4 + nota2 * 6) / 10

    if media >= 9:
        conceito = "A - Aprovado"
    elif 7 <= media < 9:
        conceito = "B - Aprovado"
    elif 3 <= media < 7:
        conceito = "C - Exame"
    else:
        conceito = "D - DP"

    print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
    print ("Desenvolvimento de Software Multiplataformas - 1º semestre Fatec ID")        
    print(f"\nMédia de Aproveitamento: {media:.0f}")
    print(f"Conceito: {conceito}")

calcular_e_mostrar_resultado()