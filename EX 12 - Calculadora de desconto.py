'''Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

valor_inicial = float(input('Valor do produto: R$'))
desconto = float(input('valor do desconto: %'))

valor_final = valor_inicial - ((desconto/100) * valor_inicial)

print('O valor do produto com desconto é de {:.2f} R$.'.format(valor_final))