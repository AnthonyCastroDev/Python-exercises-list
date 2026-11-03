preço = float(input('Preços das compras: '))
print('''formas de pagamento 
[1] à vista dinheiro/cheque 
[2] à vista no cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão] ''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 /100)

elif opção == 2:
    total = preço - (preço * 5/100)

elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f} sem juros')

elif opção == 4:
    total = preço + (preço * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de {parcela:.2f} com juros')
else:
    total = 0
    print('Opção inválida, tente novamente')

print(f'Sua compra de R${preço:.2f} vai custar no final R${total:.2f} ')


