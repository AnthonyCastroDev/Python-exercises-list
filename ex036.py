valor_casa = float(input('Qual é o valor da casa que você deseja comprar?: '))

salario = float(input('Qual é o seu salário: '))

ano = int(input('Em quantos anos você pretende pagar?: '))

prestacao = valor_casa / (ano * 12)

salario_min = salario * 30 / 100

if prestacao <= salario_min:
    print('Empretimo consedido!')
else:
    print('Emprestimo negado!')

print(f'Para pagar uma casa de {valor_casa} em {ano} a prestação será de {prestacao}')

