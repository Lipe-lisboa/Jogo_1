import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480 
x = largura / 2
y = 0 
#eixo X tem 640px
#eixo y tem 280px (no pygame p eixo y é na verticar pra baixo)

tela = pygame.display.set_mode(
    size = (largura, altura)
)

relogio = pygame.time.Clock()

pygame.display.set_caption('Jogo')

while True:
    # velocidade do jogo (quantidade de frames/segundo)
    # Quanto maior o numero de frames mais rapido o jogo roda
    relogio.tick(80)
    # preenche a tela com preto (limpa a tela)
    tela.fill((0,0,0))
    
    #pra cada interação do usuario:
    for event in pygame.event.get():
        
        #Caso o usuario queira sair so jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    
    if y == 480:
        y = 0
        
    y = y + 1
    
    #Pra cada interação o jogo tem que atualisar. Caso contrario ele trava
    pygame.display.update()