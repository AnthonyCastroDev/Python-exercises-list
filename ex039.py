from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

if idade == 18:
    print('Você está na hora exata de se alistar ')

elif idade > 18:
    saldo = idade - 18
    print( f'Você já deveria ter se alistado há {saldo} anos')
    ano = saldo - atual
    print(f'Seu alistamento foi em {ano}')

elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o seu alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}') 