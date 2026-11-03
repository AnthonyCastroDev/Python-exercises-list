primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo}", end=" ")
    termo += r
    cont += 1

