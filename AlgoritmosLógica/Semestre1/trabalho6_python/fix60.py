sexo=input("Insira seu sexo (masculino ou feminino): ") 
altura=float(input("Digite sua altura: "))
peso=float(input("Insira seu peso: "))

imc=peso/(altura*altura)

def calcular_peso (imc,sexo):
    
    if sexo == "feminino" or "f":
      if imc <19:
         return "Abaixo do peso"
      elif 19 <= imc <24:
         return "Peso ideal"
      elif imc >= 24:
         return "Acima do peso"
      
    if sexo == "masculino" or "m":
       if imc <20:
          return "Abaixo do peso"
       elif 20 <= imc <25:
          return "Acima do peso"

conceito = calcular_peso(imc, sexo)

print ("\nDesenvolvido por: Giovanna Camila Reduzino. RA: 1051392411021 | Marcelo Henrique Reduzino. RA: 1051392411005")
print ("Desenvolvimento de Software Multiplataformas - 1º semestre Fatec ID")

print(f"\nIMC:{imc:.2f}")
print(f"Conceito: {conceito}")
