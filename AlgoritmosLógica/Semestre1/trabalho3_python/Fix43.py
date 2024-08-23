nome = input("Digite o nome: ")
ra = input("Digite o RA: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

def calcular_media(nota1, nota2):
    return (nota1+nota2)/2

media = calcular_media(nota1, nota2)

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

if media>=7:
    print(f"Parabéns {nome}, você está aprovado!\nMédia: {media:.1f}.")
else:
    print(f"{nome}, você ainda tem uma chance! Estude mais para o exame.\nMédia: {media:.1f}")
    nota_exame = float(input("Digite a nota do exame: "))
    media_final = (media + nota_exame)/2
    if media_final >= 5:
        print(f"Parabéns, você aproveitou a sua chance! Está aprovado.\nMédia final: {media_final:.1f}.")
    else:
        print(f"Estude mais para a próxima. Você não alcançou o mínimo necessário.\nMédia final: {media_final:.1f}.")