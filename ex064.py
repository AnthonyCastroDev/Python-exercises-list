n = 0
cont = 0
soma = 0 

#Esse comando quer dizer que enquanto o usuario não digitar "999" o programa vai continuar rodando 
while n != 999:
#Enquanto "n" for diferente de "999"

    n = int(input("Digite um número: "))
    cont += 1 
    soma += n
    
print(f"Você digitou {cont - 1} números e a soma deles é {soma - 999}")
print("Fim do Programa!")
