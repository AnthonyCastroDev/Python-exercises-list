import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimentdo do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi}')