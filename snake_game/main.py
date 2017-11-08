#!/usr/bin/env python

"""
Hi everyone 
This is a simple car game developed using pygame witn python 3

"""
__author__  = "Mohamed Hamidat, C# and python Developer, hamidatmohamed@yahoo.fr"

import pygame
import time
import random
from snake import Snake



#display dimension
display_width = 900
display_height = 600

#car dimension
cube_width = cube_height = scale = 30
food = [0, 0]

#colors 
black = (0,0,0)
white = (255,255,255)
blue =(53, 115, 255)
red = (200,0,0)
green = (0, 200, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)
pause = False
score_game = 0

game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
#game setup 
def game_init():
    pygame.init()
    pygame.display.set_caption('Snake_game/Mohamed')  
    #game_icon = pygame.image.load('carIcon.png')
    #pygame.display.set_icon(game_icon)


##############---------FONCTIONS--------------##################

def display(count, x, y, message_format = 'score game: %d'):
    """display the score"""
   # max_dodged = 10 
    font = pygame.font.SysFont("comicsansms", 18)
    text = font.render(message_format%count, True, black)
    game_display.blit(text, (x, y))

def rect(thingX, thingY, thingW, thingH, color):
    """draw random things (car or anything)""" 
    pygame.draw.rect(game_display, color, [thingX, thingY, thingW, thingH])

def line(lineX, lineY, lineW, lineH, color):
    """draw way lines """ 
    pygame.draw.rect(game_display, color, [lineX, lineY, lineW, lineH])

def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    """display message after crash"""
    largeText = pygame.font.SysFont("comicsansms",115)
    textSurf, textRect = text_object(text, largeText)
    textRect.center = ((display_width/2) , (display_height/2))
    game_display.blit(textSurf, textRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash(x, y):
    #car_crash = pygame.image.load('images/carcrash.png')
    #game_display.blit(car_crash, ((x - 45), (y - 30)))
    #crash_sound = pygame.mixer.Sound("music/crash.wav")
    #pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",90)
    textSurf, textRect = text_object("Yo'r dead :( :('!", largeText)
    textRect.center = ((display_width/2) , (display_height/4))
    game_display.blit(textSurf, textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150,250,100,50, green, bright_green, game_loop)
        button("Quit", 550,250,100,50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg, x, y, w, h, ic, ac, action=None): 
    """message, dimension, active/inactive color"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(game_display, ac,(x, y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(game_display, ic,(x, y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    game_display.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_unpause():
    global pause
    pause = False

def game_pause():
    ############
    pygame.mixer.music.pause()
    #############
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",90)
        textSurf, textRect = text_object("Pause!", largeText)
        textRect.center = ((display_width/2) , (display_height/4))
        game_display.blit(textSurf, textRect)

        button("Continue !", 150,250,100,50, green, bright_green, game_unpause)
        button("Quit", 550,250,100,50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():

    #pygame.mixer.music.load("music/atlanta.wav")
    #pygame.mixer.music.play(-1)

    intro = True 

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(white)         
    
        largeText = pygame.font.SysFont("comicsansms", 70)
        textSurf, textRect = text_object("Let's Eat foooood !", largeText)
        textRect.center = ((display_width/2) , (display_height/2))
        game_display.blit(textSurf, textRect)

        button("GO !", 150,450,100,50, green, bright_green, game_loop)
        button("Quit", 550,450,100,50, red, bright_red, quitgame)


        pygame.display.update()
        clock.tick(15)

def get_food():
    cube_to_eat_x = random.randrange(1, (display_width - scale) // scale) * scale
    cube_to_eat_y = random.randrange(2, (display_height - scale ) // scale) * scale
    food[0] = cube_to_eat_x
    food[1] = cube_to_eat_y

def game_loop():
    global pause
    global score_game
    snake  = Snake()
    get_food()

    #pygame.mixer.music.load('music/coffee_stains.wav')
    #pygame.mixer.music.play(-1)

    score_play = 0

    snake.x = scale 
    snake.y = scale * 2

    snake.xspeed = 0
    snake.yspeed = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)
                elif event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_p:
                    pause = True
                    game_pause()
                    
        game_display.fill(white)
        # drw borders
        #right
        line(0, scale, scale, display_height, black)
        #left
        line(display_width - scale, scale, scale, display_height, black)
        #top
        line(scale, scale, display_width, scale, black)
        #buttom
        line(30, display_height - scale, display_width, scale, black)
        
        #line(display_width - scale, 0, scale, display_height, black)       
       
        rect(food[0], food[1], cube_width, cube_height, red)

        display(score_play, 150, 5)
        # display(thing_speed*60 , 5, 50, "Spd: %d px/s")    
        display(score_game, 5, 5, "Final Score: %d")

        #crash if snake touches the wall
        if snake.x >= display_width - scale or snake.x < scale or snake.y >= display_height - scale or snake.y < scale *2 :
             crash(snake.x, snake.y)
             print(snake.x, snake.y)
             score_play = 0

        #crash if it eats it self 

        if snake.can_eat(food):
            get_food()
            score_play += 1
            score_game += 1

        if snake.is_dead():
            crash(snake.x, snake.y)
        snake.update(scale)

        snake.draw(pygame, game_display)
        pygame.display.update()
        clock.tick(6)

def main():
    game_init()
    game_intro()
    game_loop()
    pygame.quit()
    quit() 

if __name__ == '__main__':
    main()


