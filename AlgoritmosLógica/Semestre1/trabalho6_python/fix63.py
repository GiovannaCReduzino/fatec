#Considere os arquivos mensagem.txt 
#desenvolva um programa em Python e determine:
#a) O tamanho da variável(mensagem.text). Qual foi o método utilizado:
#b) Criar uma lista com as palavras encontradas no arquivo mensagem.text. Qual foi o método utilizado:

import os
tam = os.path.getsize ('mensagem.txt')

arqv = open ('mensagem.txt', 'r', encoding = 'utf-8')
tamanho_conteudo = arqv.read()
palavras = tamanho_conteudo.split()

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software Multiplataformas - 1º semestre Fatec ID")

print (f"\nTamanho do conteúdo do arquivo: {tam} bytes")
print(f"Lista de palavras encontradas no arquivo '{arqv}': {palavras}")

arqv.close()