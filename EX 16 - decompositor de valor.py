
'''Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção Inteira.'''

import math

valor = float(input('digite um número real: '))
valor_int = math.trunc(valor)
fracao = valor - float(valor_int)

print("A parte inteira de ",valor,"é",math.trunc(valor),' e sua fração é ,{}'.format((fracao)))
