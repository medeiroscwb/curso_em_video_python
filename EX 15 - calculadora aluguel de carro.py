'''Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
por Km rodado.'''

kmr = float(input('Quantos kilometros foram rodados?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
preco_dia = 60.0
preco_km = 0.15

aluguel = float((kmr*preco_km)+(dias*preco_dia))
print('O custo do aluguél é de R${:.2f}'.format(aluguel))