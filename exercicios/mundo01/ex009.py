'''
Faça um programa que leia um número INTEIRO qualquer e mostre em tela a sua tabuada
'''

numero = int(input('Digite um número: '))

#regra para definir um range que inicia em 1 e vai até 10
for multiplicador in range (1,11):
    #variável que pega o número digitado e multiplica pelo valor dentro do range
    resultado = numero * multiplicador
    #saída formatada em modelo de tabuada
    print(f'{numero} x {multiplicador:2} = {resultado}')