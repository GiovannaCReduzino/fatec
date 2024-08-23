#Faça um algoritmo que mostre os descontos concedidos pela loja ABC em suas mercadorias. 
#Em compras acima de 300,00 forneça 20% de desconto, para 200,00 desconto de 15% e acima 
#de 100,00 o desconto será de 10%. Atribua valores as variáveis compra1, compra2 e compra3. 
#Mostre na tela o valor total e o valor com o devido desconto. Os mesmos devem ser solicitados 
#ao usuário, digite os valores via teclado.

print ('\nBem-vindo ao caixa! Vamos verificar se você tem desconto?')

compra1 = float(input("\nPor favor, digite o valor do primeiro produto: R$"))
compra2 = float(input("Em seguida, digite o valor do segundo produto: R$"))
compra3 = float(input("Insira o valor do terceiro produto: R$"))

valor_total = compra1 + compra2 + compra3

if valor_total > 300:
    desconto = valor_total * 0.2
    porcentagem_desconto = 20
elif valor_total > 200:
    desconto = valor_total * 0.15
    porcentagem_desconto = 15
elif valor_total > 100:
    desconto = valor_total * 0.1
    porcentagem_desconto = 10
else:
    desconto = 0
    porcentagem_desconto = 0

valor_com_desconto = valor_total - desconto
print ("\nDesenvolvido por: Giovanna Camila Reduzino (1051392411021) e Marcelo Henrique Reduzino (1051392411005)")
if porcentagem_desconto == 0:
    print(f'\nValor total da compra: R${valor_total:.2f}')
    print("Desculpe, sua compra não está nos requisitos para receber o desconto.")

else:
    print(f"\nValor total da compra: R${valor_total:.2f}")
    print(f"Desconto concedido: R${desconto:.2f} ({porcentagem_desconto:.0f}%)")
    print(f"Valor total com desconto: R${valor_com_desconto:.2f}")  