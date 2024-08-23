#Exercício Fix34
#Elabore um programa em PYTHON, que mostre os descontos concedidos pela loja ABC em 
#suas mercadorias. 
#Em compras acima de R$ 300,00 forneça 20% de desconto, entre R$ 200,00 a R$ 299,99 
#desconto de 10% e abaixo de R$ 199,99 o desconto será de 5%. 
#Mostre na tela o valor total e o valor final a pagar (com o desconto).
#Solicite os valores via teclado.

valor_compra = float (input("Insira o valor da sua compra: R$"))

if valor_compra >= 300:
    desconto = valor_compra *0.2
    porcentagem_desconto = 20

elif valor_compra >=200 <=299.99:
    desconto = valor_compra *0.1
    porcentagem_desconto = 10

else:
    desconto = valor_compra *0.05
    porcentagem_desconto = 5

valor_com_desconto = valor_compra - desconto

print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021)")

print(f"\nValor total da compra: R${valor_compra:.2f}")
print(f"Desconto concedido: R${desconto:.2f} ({porcentagem_desconto:.0f}%)")
print(f"Valor novo final a pagar: R${valor_com_desconto:.2f}")  