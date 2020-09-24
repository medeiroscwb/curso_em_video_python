'''
Manipulando cadeias de texto:
Uma cadeia de caracteres é um conjunto sequencial de
caracteres, que pode ser uma palavra, uma frase ou uma
combinação aleatória de carcteres.

vamos atribuir uma frase(sring) a uma variável chamada "frase":

frase = 'frase conceitual'

quando uma string é armazenada na memória, o
compilador atmazena cada caractere em uma posição:

|f |r |a |s |e |  |c |o |n |c |e |i |t |u |a |l |
|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|16|

dessa forma, fica fácil fazer uma alteração em um texto.

FATIAMENTO:

a forma mais simples é pegar uma letra:
Se eu usar o comando
frase(9)
eu delimito apenas o caractere na posição "9", no caso, o "n"

Para selecionar um intervalo na string, delimitamos duas posições no
comando:
frase(7,16)
>conceitua

repare que o caractere da posição 16 não foi incluído. Para incluí-lo,
indicamos a posição seguinte, mesmo que a mesma não esteja determinada
na variável:

frase(7,16)
>conceitual


por fim, podemos inserir mais um argumento nessa ferramenta:


'''

