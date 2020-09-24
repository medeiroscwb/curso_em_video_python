'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

Veja o curso completo de Python em https://www.youtube.com/playlist?list...
Veja a lista de exercícios de Python em https://www.youtube.com/playlist?list...
'''

altura = float(input("Digite a altura da sua parede:"))
largura = float(input("Digite a largura da sua parede:"))
area = altura*largura


print('sua parede tema dimensão de ',altura,'x',largura)
print('sua área é de {:.2f}m²'.format(area))
print('você utilizará {:.3f} l de tinta'.format(area/2))
