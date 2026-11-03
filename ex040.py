n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print(f'Tirando {n1} e {n2}, sua média é {media}')

if media >= 7:
    print('Você foi Aprovado')

elif media >= 5:
    print('Você ficou de Recuperação')

else:
    print('Você foi Reprovado')

