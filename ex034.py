salario = float(input('Qual salário do funcionário?: '))
aumento = 0
if salario > 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100) 

print(f'Seu salário atual é {aumento}')