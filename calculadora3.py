def menu():
    print('Menu de operações')
    print('1- Adição')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    print('5- Encerrar')
    resp = input('Escolha o tipo de cálculo que deseja: ')
    return resp

def adic():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print('A resposta de', num1, '+', num2, '=', num1 + num2)

def sub():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print('A resposta de', num1, '-', num2, '=', num1 - num2)

def mult():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print('A resposta de', num1, 'x', num2, '=', num1 * num2)

def div():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if num2 != 0:
        print('A resposta de', num1, '/', num2, '=', num1 / num2)
    else:
        print('Não é possível dividir por 0, tente outro número.')

def operacao(resp):
    if resp == '1':
        adic()
    elif resp == '2':
        sub()
    elif resp == '3':
        mult()
    elif resp == '4':
        div()
    elif resp == '5':
        print('Obrigado, volte sempre!')
        return False
    else:
        print('Por favor, escolha uma das opções acima.')
    return True

def main():
    loop = True
    while loop:
        resp = menu()
        loop = operacao(resp)

main()