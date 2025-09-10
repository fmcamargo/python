'''
Crie um progrma que leia quanto dinheiro tem na carteira e mostre quantos dólares se pode comprar
'''

#cotação que tem no google
dolarHoje = 5.43

#valor float porque é dinheiro
carteira = float(input('Quanto você tem na carteira?\nR$ '))

#converter moeda do valor que tem dividido por outra variável
cotacao = carteira / dolarHoje

#sáida formatada com as moedas
print(f'Com R$ {carteira:.2f} você pode comprar US$ {cotacao:.2f}')