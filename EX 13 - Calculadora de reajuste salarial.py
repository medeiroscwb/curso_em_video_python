'''Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario_inicial = float(input('Salario atual: R$'))
reajuste = float(input('Valor do reajuste: %'))
salario_final = salario_inicial + (reajuste/100 * salario_inicial)

print('Um funcionário com o salário de R${:.2f}, ao receber o reajuste de {}%, passará a receber R${:.2f} .'.format(salario_inicial,reajuste,salario_final))