#Exercício Fix42
#Elaborar um algoritmo (programa) que leia as notas de 5 alunos e retorne a maior nota da turma. 
#Utilizea estrutura de controle while.

def encontrar_maior_nota ():
    
    maior_nota = -1
    contador = 1
    nome_maior_nota = " "

    while contador <= 5:
        nome = input (f"\nDigite o nome do aluno {contador}: ")
        nota = float (input (f"Digite a nota do aluno {nome}: "))

        if nota > maior_nota:
            maior_nota = nota
            nome_maior_nota = nome
        
        contador += 1
    
    return nome_maior_nota, maior_nota

nome, nota = encontrar_maior_nota()

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software multiplataformas - 1º semestre Fatec ID")

print(f"\nA maior nota da turma foi '{nota}', obtida por {nome}.")


