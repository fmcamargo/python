'''
Escreva um programa que leia um valor em METROS e mostre o valor
convertido em CENTIMETROS e MILIMETROS
'''

distMetros = float(input('Digite uma distância em metros: '))

#Centímetros
distCent = distMetros*100

#Milímetros
distMili = distMetros*1000

#Saídas das conversões
print(f'A distância de {distMetros}m convertida para centímetros é {distCent}cm.')
print(f'A distância de {distMetros}m convertida para milímetros é {distMili}mm.')