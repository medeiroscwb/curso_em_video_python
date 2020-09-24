'''Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

from random import choice



a_1 = input('Nome:')
a_2 = input('Nome:')
a_3 = input('Nome:')
a_4 = input('Nome:')

lista = [a_1,a_2,a_3,a_4]

chosen = choice(lista)

print('O escolhido foi {}'.format(chosen))