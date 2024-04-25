loop = 'S'
while loop == 'S':

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    print('1- Adição')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    print('5- Encerrar')

    resp = int(input('Escolha  o tipo de calculo deseja: '))
    
    if resp == 1:
        print ('A resposta de ', num1, '+', num2, '= ', num1 + num2)
    elif resp == 2:
        print ('A resposta de ', num1, '-', num2, '= ', num1 - num2)
    elif resp == 3:
        print ('A resposta de ', num1, 'x', num2, '= ', num1 * num2)
    elif resp == 4:
        if(num1 != 0 and num2 != 0):
            print('A resposta de ', num1, '/', num2, '= ', num1 / num2)
        else:
            print('Não é possivel dividir por 0, tente outro número.')
    elif resp == 5:
        print('Obrigado, volte sempre!')
        break
    else:
        print('Por valor escolha uma das opções acima')
    loop = input('deseja calcular outros valores?(S)sim (N)não: ')    
