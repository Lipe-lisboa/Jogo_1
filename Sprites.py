import pygame
from pygame.locals import *
from sys import exit

pygame.init()


largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('sprites')

class Sapo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.add_sprite('sprites/attack_1.png')
        self.add_sprite('sprites/attack_2.png')
        self.add_sprite('sprites/attack_3.png')
        self.add_sprite('sprites/attack_4.png')
        self.add_sprite('sprites/attack_5.png')
        self.add_sprite('sprites/attack_6.png')
        self.add_sprite('sprites/attack_7.png')
        self.add_sprite('sprites/attack_8.png')
        self.add_sprite('sprites/attack_9.png')
        self.add_sprite('sprites/attack_10.png')
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        
        self.animar = False
        
    def atacar(self):
        self.animar = True
        
    def update(self):
        if self.animar:
            self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))
    
                
    def add_sprite (self, sprite):
        self.sprites.append(pygame.image.load(sprite))
    
todas_sprites = pygame.sprite.Group()    
sapo = Sapo()
todas_sprites.add(sapo)

relogio = pygame.time.Clock()

while True:
    
    relogio.tick(30)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            sapo.atacar()
    
    todas_sprites.draw(tela)
    todas_sprites.update()
    #Pra cada interação o jogo tem que atualisar. Caso contrario ele trava
    # mesma coisa que update 
    pygame.display.flip()   