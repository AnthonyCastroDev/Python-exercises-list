leitor = input('Digite o seu sexo M/F: ').upper().strip()[0]

while leitor not in 'MmFf':
    leitor = input('Dados in validos por favor digite novamente: ').upper().strip()[0]
print('Sexo rgistrado com sucesso ')    

