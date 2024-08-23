#Exercício Fix44 
#Desenvolva um programa para determinar a média geral do aluno. 
#Ele deverá receber o nome do aluno, as 2 notas obtidas do aluno nas 2 avaliações. 
#Calcular a média de aproveitamento, usando a fórmula da Média e escrever o conceito do aluno 
#de acordo com a tabela de conceitos. 
#Média é dada pela fórmula: MG = (NP1*4 + NP2*6) / 10

nome = input("Informe o nome do aluno: ")
np1 = float(input("Insira a nota da NP1: "))
np2 = float(input("Insira a nota da NP2: "))

def media_aluno(nome, np1, np2):
    media_geral = (np1 * 4 + np2 * 6) / 10

    if (media_geral >= 9) and (media_geral <= 10):
        conceito = 'Aprovado - A'
    elif (media_geral >= 7) and (media_geral < 9):
        conceito = 'Aprovado - B'
    elif (media_geral >= 3) and (media_geral < 7):
        conceito = 'Exame - C'
    elif (media_geral >= 0) and (media_geral < 3):
        conceito = 'DP - D'
    else:
        conceito = 'Nota inválida'

    return nome, media_geral, conceito

# Chamada da função para calcular a média e obter o conceito
nome, media_geral, conceito = media_aluno(nome, np1, np2)

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software multiplataformas - 1º semestre Fatec ID")

print(f"\nNome do aluno: {nome}")
print(f"Média geral: {media_geral}")
print(f"Conceito: {conceito}")