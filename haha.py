#########################################
# Game: Rabbit Jump 2k18
# Group Members: Justin W #2 and Allan
# Author: ICS2O
# Date: 31/05/2019
#########################################

import pygame
import time
pygame.init()

#set screen
WIDTH = 590
HEIGHT= 400 
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

#colours and fonts
GRIDSIZE=10
RED  =(255,  0,  0)
GREEN=(  0,255,  0)
BLUE =(  0,  0,255)
LIGHTBLUE=(122, 226, 255)
CYAN =(  0,255,255)
WHITE=(255,255,255)
BLACK=(  0,  0,  0)
GREY =(128,128,128)
LIGHTYELLOW=(249, 208, 112)
GRASSYGREEN=(52, 198, 49)
font = pygame.font.SysFont("Arial",25)

#---import pictures---"

backdrop = pygame.image.load("grassybackground.jpg")
rabbit = pygame.image.load("rabbit.png")
rabbit = pygame.transform.scale(rabbit,(75,75))
cactus = pygame.image.load("cactus.png")
cactus = pygame.transform.scale(cactus,(75,75))
tutorial = pygame.image.load("How2plAY.jpg")

#important variables
rabbitX = 80
rabbitY = 300
rabbitY2 = 375
GRAVITY = 2
rabbitSpeed = 30

cactusX = 590
cactusY = 300
cactusSpeed = 10

score = 0

#---------------------------------------#
# functions                             #
#---------------------------------------#

def background():
    picture = pygame.image.load("grassybackground.jpg")
    gameWindow.blit(picture,(0,0))

def mainMenu():
    font=pygame.font.SysFont("Futura",80)
    graphics = font.render("Rabbit Jump 2k18", 1, BLUE)
    gameWindow.blit(graphics, (50, 50))

    pygame.draw.rect(gameWindow,LIGHTBLUE,(350,180,150,80), 0)
    pygame.draw.rect(gameWindow,LIGHTBLUE,(80,180,150,80), 0)
    font=pygame.font.SysFont("Futura",40)
    graphics = font.render("Play", 1, BLACK)
    gameWindow.blit(graphics, (125, 205))
    font=pygame.font.SysFont("Futura",30)
    graphics = font.render("How to Play", 1, BLACK)
    gameWindow.blit(graphics, (365, 205))

    pygame.display.update()
    
def tutorialScreen():
    gameWindow.blit(tutorial,(0,0))
    pygame.display.update()

def gameScreen():
    gameWindow.blit(rabbit,(rabbitX,rabbitY))
    gameWindow.blit(cactus,(cactusX,cactusY))
    scoreGraphics = font.render("Score:",1,BLACK)
    finalScore = font.render(str(score),1,BLACK)
    gameWindow.blit(scoreGraphics, (10, 10))
    gameWindow.blit(finalScore,(80,10))
    pygame.display.update()

def gameOver():
    gameOver = font.render("GAME OVER", 2, BLACK)
    scoreGraphics = font.render("Score:",1,BLACK)
    finalScore = font.render(str(score),1,BLACK)
    gameWindow.blit(gameOver,(50,50))
    gameWindow.blit(scoreGraphics,(50,100))
    gameWindow.blit(finalScore,(175,100))
    pygame.display.update()

inPlay = True
screen = 1

#game loop
while inPlay:
    background()

    if screen == 1:
        #main menu
        mainMenu()

        #screen selection
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and (80<=mouseX<=230 and 180<=mouseY<=260):
                screen = 3

                #reset variables
                cactusX = 590
                cactusY = 270
                
            elif event.type == pygame.MOUSEBUTTONDOWN and (350<=mouseX<=500 and 180<=mouseY<=260):
                screen = 2

    elif screen == 2:
        tutorialScreen()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    screen = 1

    elif screen == 3:
        gameScreen()

        #jump
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and rabbitY + 75 == rabbitY2:
            rabbitSpeed = -30
#gravity
        rabbitSpeed = rabbitSpeed + GRAVITY
        rabbitY = rabbitY + rabbitSpeed
        if rabbitY + 75 >= rabbitY2:
            rabbitY = rabbitY2 - 75
            rabbitSpeed = 0

        #cactus
        cactusX = cactusX - cactusSpeed
        if cactusX == -50:
            cactusX = 590
            score = score + 1 
        pygame.display.update()

        #collision
        for j in range (cactusY,cactusY+50):
            for i in range (cactusX,cactusX+50):
                if rabbitX + 40 == i and rabbitY == j:
                    screen = 4

    elif screen == 4:
        gameOver()
        
    #exit
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
        
#---------------------------------------#
pygame.quit()
