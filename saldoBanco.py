def atualizaSaldo(saldo, valor, operacao):
    if operacao == 1:
        if valor > 0:
            saldo += valor
            print("Depósito de R$", valor, " realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Tente novamente.")
    elif operacao == 'sacar':
        if valor > 0 and valor <= saldo:
            saldo -= valor
            print("Saque de R$", valor, " realizado com sucesso.")
        elif valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido. Tente novamente.")
    return saldo

def visualizar_saldo(saldo):
    print("Seu saldo atual é: R$", saldo)

def menu():
    saldo = 3000
    
    while True:
        print("Menu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar Saldo")
        print("4. Sair")
        
        escolha = float(input("Selecione a opção desejada: "))
        
        if escolha == 1:
            valor = float(input("Digite o valor para depositar: R$"))
            saldo = atualizaSaldo(saldo, valor, 'depositar')
        elif escolha == 2:
            valor = float(input("Digite o valor para sacar: R$"))
            saldo = atualizaSaldo(saldo, valor, 'sacar')
        elif escolha == 3:
            visualizar_saldo(saldo)
        elif escolha == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
