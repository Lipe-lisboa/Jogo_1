import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480 

tela = pygame.display.set_mode(
    size = (largura, altura)
)

pygame.display.set_caption('Jogo')

while True:
    #pra cada interação do usuario:
    for event in pygame.event.get():
        
        #Caso o usuario queira sair so jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #Pra cada interação o jogo tem que atualisar. Caso contrario ele trava
        pygame.display.update()
        
        