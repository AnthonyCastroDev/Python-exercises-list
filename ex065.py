# Inicializando variáveis
soma = 0
quantidade = 0
maior = None
menor = None

while True:
    num = int(input("Digite um número inteiro: "))
    
    # Atualiza soma e quantidade de números digitados
    soma += num
    quantidade += 1

    # Atualiza maior e menor número
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

    # Pergunta ao usuário se deseja continuar
    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if continuar == 'N':
        break

# Calcula a média
media = soma / quantidade

# Exibe os resultados
print("\nResultados:")
print(f"Média dos valores: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
