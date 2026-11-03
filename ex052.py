num_primo = int(input('Digite um número inteiro: '))

for i in range( 1, num_primo + 1 ):
    if num_primo % i == 0:
        print('\033 [m', end=' ')
    else:
        print('\031 [m', end=' ')
print({i,},end=' ')

