# Base of code is from YouTube Video https://www.youtube.com/watch?v=ST-Qq3WBZBE
import scrolling_background

import pygame
import sys 

def run_game(): 
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,150))
    pygame.display.set_caption("Jumping in PyGame")

    clock = pygame.time.Clock()

    x_position, y_position = 100, 95 
    jumping = False 

    y_gravity = 0.5
    jump_height = 8
    y_velocity = jump_height

    standing_surface = pygame.transform.scale(pygame.image.load("../stimuli/dino.png"), (25, 35))
    jumping_surface = pygame.transform.scale(pygame.image.load("../stimuli/jumping_dino.png"), (25, 35))
    background = scrolling_background.Game()

    mario_rect = standing_surface.get_rect(center =(x_position, y_position))

    while True:
        for bg in background.bg: 
            bg.update(-background.speed)
            bg.show(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]: 
            jumping = True
        
        if jumping: 
            y_position -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < - jump_height:
                jumping = False
                y_velocity = jump_height
            mario_rect = standing_surface.get_rect(center =(x_position, y_position))
            screen.blit(jumping_surface, mario_rect)
        else: 
            mario_rect = standing_surface.get_rect(center = (x_position, y_position))
            screen.blit(standing_surface, mario_rect)

        pygame.display.update()
        clock.tick(60)

    