#Considere os arquivos senha.txt desenvolva um programa em Python que cadastre mais 5 senhas

arqv = open ('senha.txt', 'r', encoding = 'utf-8')
lista = arqv.readlines()
lista = [senha.split()[0] for senha in lista]

print("Digite cinco novas senhas para adicionar ao arquivo:")
for _ in range(5):
    nova_senha = input("Digite uma senha: ").split()[0]
    lista.append(nova_senha)

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software Multiplataformas - 1º semestre Fatec ID")

print("\nSenhas adicionadas com sucesso!")

print(lista)
arqv.close()