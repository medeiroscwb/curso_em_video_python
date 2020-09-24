'''
quero imprimir a mensagem:

 olá, mundo

para dados do tipo mensagem, em python, utilizamos um delimitador padrão da linguagem,
que são as aspas

 'olá, mundo'

Para imprimir a mensagem, usamos a função print(). Determinados tipos de função possuem
tipos específicos de argumentos. os argumentos vão dentro dos "()'
'''

print('olá,mundo')

'''
>olá, mundo
Números podem ser exibidos como estar sendu utilizadas aspas, ou utiliza-los em uma operação
matemática, sem utilizar aspas
'''

print(7+4)
print('7+4')
print('7'+'4')

'''
>11
>7+4
>74
'''

'''
Variáveis são uma sintaxe do código que podem receber diferentes dados
veja esses exemplos:
'''

nome = 'felipe'  #atribui a string 'felipe' à variável "nome"
idade = 31 #atribui o valor inteiro 31 à variável "idade"
peso = 75.5 #atribui o valor flutuante 75.5 à variável "peso"

print(nome,idade,peso)

'''
Podemos receber essas informações durante a execução do programa, utilizando a função 
INPUT()
'''

nome = input('nome:')
idade = input('idade:')
peso = input('peso:')

print('nome:',nome)
print('idade:',idade)
print('peso:',peso)