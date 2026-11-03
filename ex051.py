termo1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

decimo = termo1 + (10 - 1) * r

for i in range(termo1, decimo + r, r):
    print(i, end=' ')
