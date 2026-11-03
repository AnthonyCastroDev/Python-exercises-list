velocidade_car = int(input('Digite a velocidade do carro?'))
multa = (velocidade_car - 80) * 7
if velocidade_car > 80:
    print('Você foi multado!')
    print(f'Você deve pagar uma multa de R$!{multa:2f}')
else:
    print('Tenha um bom dia! Dirija com segurança!')


