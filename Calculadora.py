num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print('RESULTADOS')
print('Adição: ', num1 + num2)
print('Subtração: ', num1 - num2)
print('Multiplicação: ', num1 * num2)

if(num1 != 0 and num2 != 0):
    print('Divisão: ', num1 / num2)
else:
    print('Não é possivel dividir por 0, tente outro número.')    