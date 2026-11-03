
h_idade = 0
nomevelho = 0
somaidade = 0
mediaidade = 0

for i in range (1,5):
    print(F'----{i} PESSOA----')
    nome = input('nome?: ').strip()
    idade = int(input('Idade: '))
    sexo = input('F/M: ').strip()
    
    somaidade += 1
    mediaidade = somaidade / 4
    if i == 1 and sexo in 'Mm':
        h_idade = idade
        nomevelho = nome 
    if sexo in 'Mm' and idade > h_idade:
          h_idade = idade
          nomevelho = nome 

        
        
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {h_idade} anos e se chama {nomevelho}')
