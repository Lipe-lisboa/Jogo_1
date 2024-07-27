import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480 

#eixo X tem 640px
#eixo y tem 280px (no pygame p eixo y é na verticar pra baixo)

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
            
        pygame.draw.rect(tela, (255,0,0), (200, 300, 40, 50))
        pygame.draw.circle(tela, (0,0,255), (300, 260), 40)
        pygame.draw.line(tela, (0,255,0), (390, 0),(390, 600), 10)
        
        #Pra cada interação o jogo tem que atualisar. Caso contrario ele trava
        pygame.display.update()