# Função para obter o primeiro e último nome de uma pessoa
def obter_primeiro_e_ultimo_nome(nome_completo):
    # Divide o nome completo em uma lista de palavras
    nomes = nome_completo.split()
    
    # Obtém o primeiro nome (primeira palavra da lista)
    primeiro_nome = nomes[0]
    
    # Obtém o último nome (última palavra da lista)
    ultimo_nome = nomes[-1]
    
    return primeiro_nome, ultimo_nome

# Solicita o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# Chama a função e obtém os resultados
primeiro_nome, ultimo_nome = obter_primeiro_e_ultimo_nome(nome_completo)

# Exibe o primeiro e o último nome
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
