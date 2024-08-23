dia = int(input("Digite um numero inteiro entre '1 e 7': "))
mensagem = "Hoje é um bom dia para aprender Python"
match dia:
    case 1:
        print(" Domingo. " + mensagem)
    case 2:
        print(" 2da Feira. " + mensagem)
    case 3:
        print(" 3ça Feira. " + mensagem)
    case 4:
        print(" 4ta Feira. " + mensagem)
    case 5:
        print(" 5ta Feira. " + mensagem)
    case 6:
        print(" 6ta Feira. " + mensagem)
    case 7:
        print(" Sabado. " + mensagem)
    case _:
        print(" Dia invalido")