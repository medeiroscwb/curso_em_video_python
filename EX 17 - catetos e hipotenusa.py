'''Faça um programa que leia o comprimento do cateto adjacente e do cateto oposto de  um
triangulo retângulo, calcule e mostre o comprimento da hipotenusa'''

#cat_a = float(input('comprimento do cateto adjacente: '))
#cat_o = float(input('comprimento do cateto oposto: '))

#hip = (cat_a**2+cat_o**2)**(1/2)

#print('A soma dos quadrados dos catetos "{}" e "{}" é igual ao quadrado da hipotenusa "{:.2f}"'.format(cat_a,cat_o,hip))


'''alternativa'''

#import math  ou
from math import hypot

cat_a = float(input('comprimento do cateto adjacente: '))
cat_o = float(input('comprimento do cateto oposto: '))
hip = hypot(cat_a,cat_o)

print('A soma dos quadrados dos catetos "{}" e "{}" é igual ao quadrado da hipotenusa "{:.2f}"'.format(cat_a,cat_o,hip))
