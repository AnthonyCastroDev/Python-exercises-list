larg = float(input('largura a parede: '))
alt = float(input('altura da parede:'))
area = larg * alt 
print('sua parede tem a dimensão de {}x{} e sua área é de {} metros quadrados.'.format(larg, alt, area))
tinta = area/2 
print('pra pintar essa parede você pecisará de {}L de tinta.'.format(tinta))