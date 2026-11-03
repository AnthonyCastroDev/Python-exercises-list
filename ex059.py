#Crie um programa que leia dois valores e mostre um menu na tela:

while True:
    # Lendo os dois valores iniciais
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    while True:
        print("\nMENU:")
        print("[1] Somar")
        print("[2] Multiplicar")
        print("[3] Maior número")
        print("[4] Inserir novos números")
        print("[5] Sair do programa")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print(f"Resultado da soma: {num1 + num2}")
        elif opcao == '2':
            print(f"Resultado da multiplicação: {num1 * num2}")
        elif opcao == '3':
            maior = max(num1, num2)
            print(f"O maior número é: {maior}")
        elif opcao == '4':
            break  # Sai do menu para inserir novos números
        elif opcao == '5':
            print("Encerrando o programa...")
            exit()  # Finaliza o programa
        else:
            print("Opção inválida! Tente novamente.")
