from datetime import date

ano_atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano_atual - nasc 

print(f'O atleta tem {idade} anos')

if idade <= 9:
    print('classivicação: Mirim')
elif idade <= 14:
    print('clasificação: Infântil')
elif idade <= 19:
    print('classificação: Junior')
elif idade <= 25:
    print('classificação: Sênior')
else:
    print('Master')

