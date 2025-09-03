'''
+ adição
- subtração
* multiplicação
/ divisão
** potencia ou exponenciação
// divisão inteira
% resto da divisão ou módulo

ORDEM DE PRECEDÊNCIA

1. ()
2. **
3. * / // %
4. + -

'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1** n2

print(f'A soma é {s} \n o produto multiplicado é {m} \n a divisão é {d:.3f} \n o resto da divisão é {di:.3f} \n e a potência é {e}')