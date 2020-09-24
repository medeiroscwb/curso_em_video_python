'''
Vamos começar com um teste:

n1=input('digite um numero:')
n2=input('digite ouro número:')
s=n1+n2
print(s)

>digite um numero:2
>digite ouro número:3
>23

Como podemos perceber, o console não retornou a soma de 2 e 3, mas ele fez uma concatenação
com os dois algoritmos. Isso acontece porque cada variável, recebe uma informação de um
determinado TIPO PRIMITIVO.

Estes são os 4 principais tipo primitivos:

STRING: textos que podem ou não conter algarismos. uma string deve ser definida por aspas
simples
INT:Valores numéricos do conjunto dos numeros inteiros
FLOAT: Valores numéricos do conjunto dos numeros racionais
BOOL: Valores do tipo Verdadeiro ou Falso

Podemos verificar o tipo da variável com o comando

type(variável)

colocando a variável como argumento

Podemos também, mudar o tipo primitivo do dado de uma variável com as funções

str()            int()           float()              bool()

Colocando a variável como argumento

Mascara:
Um dado do tipo STRING pode utilizar uma "máscara", que é uma forma de inserir variáveis
dentro de uma string +- fixa

podemos fazer isso dessa forma:

n1=3
n2=5

print('A soma dos números {} e {} é igual a '.format(n1,n2),n1+n2,'.')

>A soma dos números 3 e 5 é igual a 8 .

Prática:
'''

'''n1 = input('digite um valor:') #imput de um valor qualquer
print(type(n1)) #verifica o tipo do imput. Um input sempre vem no formato STR
int(n1) #esse comando transforma o dado de n1 em tipo INT, mas não guarda na memória
print(type(int(n1))) #esse comando o tipo da variável já convertida
print('podemos converter o tipo primitivo do dado já no momento do input:')
n2 = int(input('digite outro número: '))
print(type(n2)) #><class 'int'>
#mascara
print('A soma dos números {} e {} é igual a '.format(n1,n2),int(n1)+n2,'.')'''

''' Desafio: feça um programa que receba um input e verifique as informações possíveis 
sobre a variável'''

variavel = input('digite algo: ')
print('é alfanumérico?',variavel.isalnum())
print('é alfabético?',variavel.isalpha())
print('é ascii?',variavel.isascii())
print('é decimal?',variavel.isdecimal())
print('é digito?',variavel.isdigit())
print('é identificador?',variavel.isidentifier())
print('é minúsculo?',variavel.islower())
print('é numérico?',variavel.isnumeric())
print('é imprimível?',variavel.isprintable())
print('é espaço?',variavel.isspace())
print('é titulo?',variavel.istitle())
print('é maiúsculo?',variavel.isupper())