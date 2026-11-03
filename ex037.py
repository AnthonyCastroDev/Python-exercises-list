num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: [1] Bináro [2] Octal [3] Hexdecimal')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} convertido para Binário é: {bin(num)}')

elif opção == 2:
    print(f'{num} convertido para Octal é: {oct(num)}')

elif opção == 3:
    print(f'{num} conertido para Hexdecimal é: {hex(num)}')

else:
    print('Opção inválida tente novamente!')


    