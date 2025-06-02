def mostrar_menu():
    print("\nEscolha uma opção: ")
    print("1 - Saldo")
    print("2 - Sacar dinheiro")
    print("3 - Sair")

def ver_saldo(saldo):

    print(f"\nSeu saldo atual é: R${saldo:.2f}")

   
def sacar_dinheiro(saldo):
    valor = float(input("\nDigite o valor para saque: "))

    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor % 10 != 0:
        print("O valor do saque deve ser múltiplo de 10!")
    else:
        saldo -= valor
        print("Saque realizado com sucesso")

    return saldo   

def caixa_eletronico():
    saldo = 1000
    print("Bem-vindo ao Caixa Eletrônico!")

    while True:

        mostrar_menu()

        opcao = input(">> ")

        if opcao == "1":
            ver_saldo(saldo)
        elif opcao == "2":
            saldo = sacar_dinheiro(saldo)
        elif opcao == "3":
            print("\nObrigado por usar o caixa eletrônico!")
        else:
            print("\nOpção inválida. Tente novamente.")
        break

caixa_eletronico()
