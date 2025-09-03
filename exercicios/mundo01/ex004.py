'''
DESAFIO

Faça um programa que leia algo pelo teclado e mostre
na tela o tipo primitivo do objeto e todos os seus métodos
'''

n = input('Digite algo: ')

print('O tipo primitivo dessa variável é' , type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('Está em minúsculas?', n.islower())
print('Está maiusculas?', n.isupper())