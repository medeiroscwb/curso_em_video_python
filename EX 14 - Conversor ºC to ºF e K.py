'''Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

celcius = float(input('Temperatura em ºC:'))
kelvin = celcius + 273.15
fahrenheit = (celcius * 9/5) + 32

print('{:.1f}ºC'.format(celcius))
print('{:.1f}ºF'.format(fahrenheit))
print('{:.1f} Kelvin'.format(kelvin))