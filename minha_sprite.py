import pygame
from pygame.locals import *
from sys import exit

pygame.init()


largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('sprites')

class Personagem(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.add_sprite('Sprite_Homem_terno/sprite_0.png')
        self.add_sprite('Sprite_Homem_terno/sprite_1.png')
        self.add_sprite('Sprite_Homem_terno/sprite_2.png')

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32*6, 32*6))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 70, 270
    
        
    def update(self):
        self.atual += 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
            self.animar = False
        
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32*6, 32*6))

                
    def add_sprite (self, sprite):
        self.sprites.append(pygame.image.load(sprite))
    
todas_sprites = pygame.sprite.Group()    
personagem = Personagem()
todas_sprites.add(personagem)

img_fundo = pygame.image.load('img_fundo.webp').convert()
img_fundo = pygame.transform.scale(img_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    
    relogio.tick(15)
    tela.fill((0,0,0))
    tela.blit(img_fundo, (0,0))
    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            exit()
    
    todas_sprites.draw(tela)
    todas_sprites.update()
    #Pra cada interação o jogo tem que atualisar. Caso contrario ele trava
    # mesma coisa que update 
    pygame.display.flip()   