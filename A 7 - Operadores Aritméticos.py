'''
operadores aritméticos:

+ Adição
- Subtração
/ Divisão
// Divisão inteira
% Resto da divisão
* multiplicação
** exponenciação
= Atribuição
== teste de igualdade

print(5+2==7)
>true
--*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*--
print(5/2)
print(5//2)
print(5%2)

>2,5 #divisão
>2 #divisão inteira
>1 #resto da divisão
--*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*--
A ordem de precedência é ()>**>*>/>//>%>+>-
ordem de procedência definida é sempre definida por (), e podem haver parenteses dentro
de parenteses

print(5+3*2)
print((5+3)*2)

>11
>16
--*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*--


Prática:

CONSOLE:

>>3+3*2 (3+(3*2))
>9

>>5**2  (5 ao quadrado)
>25

>>5**3 (5 ao cubo)
>125

>>19//2  (19/2 divisão inteira, ignora o resto)
>9

>>19/2  (19/2 divisão com resto)
>9.5

356**5432
29949459472755411542742395921864527288577744251562579672651411472929332762346757414621
97276140281378076104197478040278155258802145003291543108524861772562216804689577473451
88448496710280290642430812349191584267992568576233090288635625242443575935950699596494
10687691196329117149131354744906794698189950762720598162881796538327755500515792461418
05756438103525871394307366091886056162843100028959029306756072026200167830563505522933
59964720129380746644921703599261851138914600431460969358487638284228391153109246484214
83183800888350810991978152594974537123278015970424416533172650859022667033762699355275
61476342751324688081551006538102681519509117539979017559888296170295515952767762903550
45333142976921661730904993893205016774299276210775042953582429267369060675848963904788
(o tamanho do número só é restrito ao tamanho da memória)

>>18%2 (resto da divisão 18/2 , que no caso é 0
>0

>>19%2 (resto da divisão 19/2, que é 0.5)
>0.5

>>pow(4,3) (outra forma de solicitar potencia(4 ao cubo))
>64

>>81**(1/2)  (raíz quadrada de 81)
>9

>>1000**(1/3)  (raiz cúbica de 1000)
>9.999999999999998 (não sei porque volta esse valor quebrado, deveria ser 10)

'oi' + "olá" (aplicado a strings, o "+" realiza concatenação)
'oiolá'

'oi'*5 (multiplicar uma string por um int, realiza várias impressões)
'oioioioioi'
'''

#n1 = int(input('valor 1:'))
#n2 = int(input('valor 2:'))
#print('A soma de {} e {} vale {}'.format(n1,n2,n1+n2))

#-----------------------------------------------------------------------------------

#print('Escolha dois valores a serem calculados:')
#n1 = int(input('valor 1:'))
#n2 = int(input('valor 2:'))

#s = n1 + n2
#m = n1 * n2
#d = n1 / n2
#di = n1 // n2
#e = pow(n1,n2)

#print('A soma é {}, a multiplicação é {}, a divisão é {:.1f}'.format(s,m,d)) ##":.1f" dentro da chave indica que quero somente uma casa decimal do float
#print('A divisão inteira de {} por {} é {} e a potência de {} à {} é {}'.format(n1,n2,di,n1,n2,e))

#-------------------------------------------------------------------------------------
"""desafio: Ex 5 ao 15 """