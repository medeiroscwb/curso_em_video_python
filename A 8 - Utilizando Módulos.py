'''
Utilizando Módulos:
Módulos são programas feitos em python que trazem uma série de funcionalidades e soluções
que já foram testadas e aprovadas pela comunidade Python.
Podemos importar um módulo, ou biblioteca utilizando o comando IMPORT. É convencionado
importar os módulos necessários nas primeiras linahs do programa.

>import math (importa a biblioteca "math")

>from math import pi (de dentro da biblioteca "math", importa a função "pi")

Bibllioteca math:
ceil (arredonda para cima)
floor (arredonda para baixo)
trunc (truncar, elimina da virgula para frente)
pow (potência)
sqrt (squareroot, raiz quadrada)
factorial (fatoração)

'''
#import math
#num = 9
#raiz = math.sqrt(num) (importando dessa forma, é preciso colocar "math." antes da função)
#print(raiz)
#>3.0

#from math import sqrt
#num = 9
#raiz = sqrt(num) (dessa forma não é preciso referenciar o modulo MATH)
#print(raiz)
#>3.0

'''Podemos consultar um manual de instruções dos modulos distribuídos em 
https://docs.python.org/3/'''


import random

num = random.random()
print(num)
> numero racional aleatório entre 0 e 1

num = random.randint(1,1000)
print(num)
> numero inteiro aleatório entre 0 e 1000

'''
digite import, segure ctrl e aperte espaço para obter a lista dos módulos padrão, 
que já vem com a instalação do python + módulos instalados

Além dos módulos padrão, podemos baixar e até mesmo publicar módulos em
pypi.org

Desafio: Ex 16 ao 21'''