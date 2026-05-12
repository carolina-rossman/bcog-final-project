import pygame

class Display():
    screen_size = (800, 600)
    def __init__(self, screen):
        pygame.init()
        my_font = pygame.freetype.SysFont('Arial', 65)
        text_surface = my_font.render('You Died', False, (0, 0, 0))
        screen.blit(text_surface, (0, 0))