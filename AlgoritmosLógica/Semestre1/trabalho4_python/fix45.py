#Exercício Fix45 
#Desenvolva um programa que só permita o acesso a pessoas autorizadas (professor, via autenticação) 
#para posteriormente realizar a média do aluno. 
#Para isto Considere o programa criado no Fix44. 
#Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, 
#depois faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo.

senha_correta = "fatec2024" 
tentativas = 3
professor = input (str("\nProfessor, insira seu nome para efetuação de login: "))

while tentativas > 0:
    
    senha = input("\nDigite sua senha: ")
    
    if senha == senha_correta:

        print (f"\nBem-vindo, professor {professor}!")
        
        nome = input("\nDigite o nome do aluno: ")
        ra = input("Digite o RA do aluno: ")
        turma = input("Digite a turma do aluno: ")
       
        np1 = float(input("Insira a nota da NP1: "))
        np2 = float(input("Insira a nota da NP2: "))

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
        
        print("\nInformações do Aluno:")
        print(f"Nome: {nome}")
        print(f"RA: {ra}")
        print(f"Turma: {turma}")
        print(f"Média: {media_geral}")
        print(f"Conceito: {conceito}")
        break
    
    else:
        print("Senha incorreta. Tente novamente.")
        tentativas -= 1
    
if tentativas == 0:
    print("\nNúmero máximo de tentativas excedido. Acesso negado.")

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software multiplataformas - 1º semestre")