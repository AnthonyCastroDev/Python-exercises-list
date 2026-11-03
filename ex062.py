# Solicita os valores iniciais
primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))

# Inicializa as variáveis
termo = primeiro
cont = 1
total = 0
mais = 10  # Começa exibindo 10 termos

# Loop principal para exibir os termos da PA
while mais != 0:
    total += mais  # Atualiza o total de termos a serem exibidos
    
    while cont <= total:
        print(termo, end=" ")
        termo += r  # Calcula o próximo termo
        cont += 1

    print("\nPausa")  # Indica uma pausa antes de perguntar ao usuário

    # Pergunta quantos termos extras exibir
    mais = int(input('Quantos termos você quer mostrar a mais? (Digite 0 para sair): '))

print("Progressão finalizada!")
