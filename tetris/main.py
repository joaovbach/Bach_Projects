import sys, pygame
import random
from ControlaFormas import Controla


pygame.init()


tela = pygame.display.set_mode([500,500])
game = Controla()
cadencia = 0

def apagaTela():
    pygame.draw.rect(tela,[0,0,0],[0,0,1000,1000])

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game.criaForma(0)


            if event.key == pygame.K_2:
                apagaTela()
                game.renderFormas(pygame,tela)

            if event.key == pygame.K_3:
                game.down()

            if event.key == pygame.K_RIGHT:
                game.formasNaTela[0].move("RIGHT")

            if event.key == pygame.K_LEFT:
                game.formasNaTela[0].move("LEFT")
    
    if cadencia < 500:
        cadencia+=1
    else:
        apagaTela()
        #game.down()
        game.renderFormas(pygame, tela)
        cadencia=0
    
    pygame.display.update()
