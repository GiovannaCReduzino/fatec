#Considere os arquivos email.txt desenvolva um programa em Python que cadastre mais 3 E-MAILS

arqv = open ('email.txt', 'r', encoding = 'utf-8')
lista = arqv.readlines()
lista = [email.split()[0] for email in lista]

print("Digite três novas para adicionar ao arquivo:")
for _ in range(3):
    novo_email = input("Digite um e-mail: ").split()[0]
    lista.append(novo_email)

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software Multiplataformas - 1º semestre Fatec ID")

print("\nE-mails adicionados com sucesso!")
print(lista)
arqv.close()
