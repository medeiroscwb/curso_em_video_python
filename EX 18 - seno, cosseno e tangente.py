'''Exercício Python #018 - Seno, Cosseno e Tangente: faça um programa que leia um angulo
qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.'''

import math

while('true'):
    a = int(input('Angulo: '))
    sin = math.sin(a)
    cos = math.cos(a)
    tan = math.tan(a)

    print('O SENO de {} é {}'.format(a,sin))
    print('O COSSENO de {} é {}'.format(a,cos))
    print('A TANGENTE de {} é {}'.format(a,tan))
