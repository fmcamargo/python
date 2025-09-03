'''
Crie um programa que leia duas notas de um aluno, calcule e mostre sua média
'''

nomeAluno = input('Nome do estudante: ')
penultimaNota = int(input(f'Digite sua penúltima nota: '))
ultimaNota = int(input(f'Digite sua última nota: '))

notaSoma = penultimaNota + ultimaNota

mediaFinal = notaSoma / 2

print(f'As duas últimas notas do estudante {nomeAluno} foram\nPenúltima nota: {penultimaNota}\nÚltima nota: {ultimaNota}\nPortanto sua média é de {mediaFinal}')