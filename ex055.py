peso_menor = 0 
peso_maior = 0

for i in range(1,6):
    peso = float(input(f'Digite o {i} peso: '))
    if i == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso_maior > peso:
            peso_maior = peso 
        if peso_menor < peso:
            peso_menor = peso

print(f'O maior peso é {peso_maior}kg') 
print(f'O menor peso é {peso_menor}kg')