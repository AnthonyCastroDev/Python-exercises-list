num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'A unidade é {u}: ')
print(f'A dezena é {d}: ')
print(f'A Centena é {c}: ')
print(f'O Milhar é {m}: ')