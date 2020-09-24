'''Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar.'''

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar_americano = real/4.61
euro = real/6.64
peso_uruguaio = real/0.13
yuan = real/0.81

print('com R$ {:.2f} você pode comprar:'.format(real))
print('U$$ {:.2f}'.format(dolar_americano))
print('EUR {:.2f}'.format(euro))
print('U$ {:.2f}'.format(peso_uruguaio))
print('YU {:.2f}'.format(yuan))
