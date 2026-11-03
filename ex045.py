#programa jokenpô:

#primeiro importo a biblioteca random para fazer a escolha do computador
import random

escolhas = ['pedra', 'papel', 'tesoura']

escolha_usuario = input('Escolha pedra pepel ou tesoura: ').lower()

if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
    print('Escolha inválida ')

else:
    escolha_computador = random.choice(escolhas)
    print(f'Você escolheu {escolha_usuario} e o computador escolheu {escolha_computador} ',end='')

    if escolha_computador == escolha_usuario:
        print('Empate')
    
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você venceu!")
    else:
        print("Computador venceu!")
    

print("Obrigado por jogar!")