import pygame
import pygame.freetype
import sys


class Display:
    window = pygame.display.set_mode((800, 600))

    def __init__(self, window):
        pygame.init()
        self.font = pygame.freetype.SysFont("Arial", 65, bold=True)
        self.background = pygame.Surface(window.get_size())
        self.red = [255, 99, 71]
        self.background.fill(self.red)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            window.blit(self.background, (0, 0))
            text_surface, rect = self.font.render("You Died")
            window.blit(text_surface, (250, 250))
            pygame.display.flip()

        pygame.quit()

    def buttons(self):
        pygame.draw.rect(self.window, (0, 200, 0), self.restart_button)
        pygame.draw.rect(self.window, (200, 0, 0), self.quit_button)
        self.button_font = pygame.freetype.SysFont("Arial", 20, bold=True)


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    Display(window)


if __name__ == "__main__":
    main()
