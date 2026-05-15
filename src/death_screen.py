import pygame
import pygame.freetype
import sys
import base_dino


class Display:
    window = pygame.display.set_mode((800, 600))

    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((800, 600))
        self.font = pygame.freetype.SysFont("Arial", 65, bold=True)
        self.background = pygame.Surface(window.get_size())
        self.red = [128, 0, 0]
        self.background.fill(self.red)
        self.restart_button = pygame.Rect(300, 250, 200, 50)
        self.quit_button = pygame.Rect(300, 350, 200, 50)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.window.blit(self.background, (0, 0))
            text_surface, rect = self.font.render("You Died")
            self.window.blit(text_surface, (250, 250))
            pygame.display.flip()
        pygame.quit()

    def create_buttons(self):
        window = pygame.display.set_mode((800, 600))
        pygame.draw.rect(window, (0, 200, 0), self.restart_button)
        pygame.draw.rect(window, (200, 0, 0), self.quit_button)
        self.button_font = pygame.freetype.SysFont("Arial", 20, bold=True)
        restart_text = self.button_font.render("Restart", True, (255, 255, 255))
        quit_text = self.button_font.render("Quit", True, (255, 255, 255))
        self.window.blit(window, (self.restart_button.x, self.restart_button.y))
        self.window.blit(window, (self.quit_button.x, self.quit_button.y))

    def restart(self):
        self.window = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        running = True
        while running:
            self.__init__()
            self.create_buttons()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_screen = base_dino.run_game()
                    new_screen.restart()
                    if self.restart_button.collidepoint(event.pos):
                        base_dino.run_game()
                    if self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update
            clock.tick(120)


def main():
    window = pygame.display.set_mode((800, 600))
    my_display = Display()
    my_display.restart()


if __name__ == "__main__":
    main()
