import pygame
import os
import sys
from random import randint

pygame.init()

 #ventana
ventana = pygame.display.set_mode((800, 450))
pygame.display.set_caption("wWZ")
icono = pygame.image.load("spritezombie2.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondoestesi.jpg").convert()
ventana.blit(fondo, (0, 0))
reloj = pygame.time.Clock()


# variables

velocidad = 1
direccion = True
posX, posY = randint(1,500), randint(1,150)

#Jugador
class Player:
    def __init__(self,alto=40,ancho=40,velocidad=1,coordenadasInicio=(300,300), color=(255,255,255)):
        self.image = pygame.image.load(os.path.join('mirillaestesi.png'))
        self.image = pygame.transform.scale(self.image,(60,60))
        self.hitbox = pygame.Rect(0, 0, alto, ancho)
        self.hitbox.center = coordenadasInicio
        self.velocidad = velocidad
        self.color = color


#####movimiento con teclado
    def mov(self,up,down,left,right):
        keys = pygame.key.get_pressed()
        self.hitbox.x += (keys[right] - keys[left]) * self.velocidad
        self.hitbox.y += (keys[down] - keys[up]) * self.velocidad
    
    #def mov1(self):
     #   mouse_pos =pygame.mouse.get_pos
      #  Player.rect.x =mouse_pos[0]
       # Player.rect.y = mouse_pos[0]

    


#jugador = Player(40,40,1,(300,300),(255,0,0))

#NPC 

class npc:
    
    def __init__(self,alto=100,ancho=100,velocidad= (velocidad)-1, coordenadas=(posX,posY), color=(255,255,255)):
        self.image= pygame.image.load(os.path.join('zombie1.png'))
        self.image = pygame.transform.scale(self.image,(200,200))
        self.hitbox = pygame.Rect(0, 0, alto, ancho)
        self.hitbox.center = coordenadas
        self.velocidad = velocidad
        self.color = color

jugador = Player(40,40,1,(300,300),(255,0,0))
zombie = []
zombie = npc(100,100,0,(posX,posY),(0,255,0))


# sprites
#all_sprite_list= pygame.sprite.Group()
#Player= Player()
#all_sprite_list.add(move1)


  

#bucle

while True:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        # si detecta mov de teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                jugador.image = pygame.image.load(os.path.join('sangre.png'))
                jugador.image = pygame.transform.scale(jugador.image,(50,50))
                #jugador.shoot()
        

    jugador.mov(pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT)
    #jugador(pygame.sprite.spritecollide(jugador, zombie, False))
    
  

    ventana.fill((255,255,255))
    ventana.blit(fondo, (0, 0))
    ventana.blit(zombie.image,zombie.hitbox)
    ventana.blit(jugador.image,jugador.hitbox)
    

    
    
    #enemigo.draw()
    pygame.display.update()
