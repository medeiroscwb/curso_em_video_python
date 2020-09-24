'''Exercício Python 021: Faça um programa
em Python que abra e reproduza o áudio de um arquivo
MP3.'''

'''import pygame
pygame.init()
pygame.mixer.music.load('tgn.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

'''Por alguma incompatibilidade com o seu sistema, 
  quando o pygame é inicializado, ele requer mais coisas
  do que estamos dando. A alternativa mais fácil é 
  utilizarmos apenas o mixer e procurarmos outra forma
  de manter o programa funcionando, como import time 
  junto com time.sleep(x) ou apenas um input. Aqui 
  vai minha sugestão para não precisarmos importar 
  mais nada e conseguirmos testar o som:'''

from pygame import mixer
mixer.init()
mixer.music.load('tgn.mp3')
mixer.music.play()
input('Agora você escuta?')