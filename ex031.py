distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(F'O preço da sua viagem será de R${preço:.2f} reais')
