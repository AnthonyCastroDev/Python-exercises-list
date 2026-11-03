from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0 

for i in range(1,8):
    ano_nasc = int(input(f'ano de nascimentoda {i} pessoa: '))
    
    idade = atual - ano_nasc
    
    if idade >= 18:
        totmaior += 1 

    else:
        totmenor += 1

print(f'Ao todo {totmaior} maiores de idade, e {totmenor} menores de idade')


