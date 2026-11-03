peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2 )

print(f'O seu imc é {imc:.1f},', end=' ')

if imc <= 18.5:
    print('você está com Baixo peso!')
elif imc < 25:
    print('Parabéns você está no Peso normal!')
elif imc < 30:
    print('você está com Sobrepeso!')
elif imc <= 40:
    print('você está com Obesidade!')
else:
    print('você está com Obesidade mórbida!')


