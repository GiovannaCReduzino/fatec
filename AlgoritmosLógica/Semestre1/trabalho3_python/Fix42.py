nome = input("Digite o nome: ")
ra = input("Digite o RA: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")

def calcular_media(nota1, nota2):
    return (nota1+nota2)/2

media = calcular_media(nota1, nota2)

if media>=7:
    print(f"\nParabéns {nome}, você está aprovado!\nMédia: {media:.1f}.")
else:
    print(f"\n{nome}, você ainda tem uma chance! Estude mais para o exame.\nMédia: {media:.1f}")
    