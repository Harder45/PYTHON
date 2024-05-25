eletro = str(input('Informe o nome do eletrônico eletrônico:'))
tempo = float(input('Tempo de uso: '))
kh_w = 0.90 #Preço do Kw/H
gasto = tempo * kh_w #calcula o gasto
print(f'Seu(a) {eletro} teve um gasto de R$ {gasto :.2f} com {tempo} Horas de uso')
