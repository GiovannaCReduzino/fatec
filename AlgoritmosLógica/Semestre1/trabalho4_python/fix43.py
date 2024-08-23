#Exercício Fix43 
#Elaborar um algoritmo (programa) que determine se a pessoa está com no seu Peso Ideal (ou não) e IMC. 
#Onde o usuário deverá digitar o peso, o sexo e a altura de uma determinada pessoa. 
#Após a execução, deverá exibir se esta pessoa está ou não com seu peso ideal. Veja tabela (a) e (b) da relação peso/altura². 
#Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, 
#depois faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo.

sexo = input("Insira seu sexo (masculino ou feminino): ")
altura = float(input("Digite sua altura: "))
peso = float(input("Insira seu peso: "))

imc = peso / (altura * altura)

def calcular_peso(imc, sexo):

    if sexo == "feminino" or "f":
        if imc < 19:
            return "Abaixo do peso"
        elif 19 <= imc < 24:
            return "Peso ideal"
        elif imc >= 24:
            return "Acima do peso"

    if sexo == "masculino" or "m":
        if imc < 20:
            return "Abaixo do peso"
        elif 20 <= imc < 25:
            return "Peso ideal"
        elif imc >= 25:
            return "Acima do peso"

conceito = calcular_peso(imc, sexo)

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software multiplataformas - 1º semestre Fatec ID")

print(f"IMC:{imc:.2f}")
print(f"Conceito: {conceito}")
