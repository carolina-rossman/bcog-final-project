import pygame 
import sys
import powers_screen
# all the screen.py are essentially the same thing all based on start_screen.py
class Display(): 
    # setting up screen size
    screen_size = (800, 600)
    def __init__(self):
        pygame.init()
        self.screen_size_x = self.screen_size[0]
        self.screen_size_y = self.screen_size [1]
        # creating canvas/display given screen size 
        self.canvas = pygame.display.set_mode(self.screen_size)
        # loading background image and scaling it to fit screen size
        self.background_image = pygame.image.load("../stimuli/instructions_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_size))
        # setting th eposition of the start and quit buttons
        self.start_button = pygame.Rect(80, 500, 200, 50)
        self.quit_button = pygame.Rect(520, 500, 200, 50)
        #captions what the screen is in this case the Instructions Screen 
        pygame.display.set_caption("Instructions Screen")
                
    def init_window(self):
        # creates the background
        self.canvas.blit(self.background_image, (0,0))

    def create_interface_buttons(self): 
        # creates 2 buttons a start and a quit button 
        pygame.draw.rect(self.canvas, (0, 200, 0), self.start_button)
        pygame.draw.rect(self.canvas,(200, 0, 0), self.quit_button)
        # sets a font for the buttons
        self.button_font = pygame.font.SysFont("Arial", 20, bold=True)
        # creates the text for the buttons, bolds it and makes the text white 
        start_text = self.button_font.render ("Next!", True, (255, 255, 255))
        quit_text = self.button_font.render ("Quit", True, (255, 255, 255))
        # finsihing creating the buttons visually no function yet 
        self.canvas.blit (start_text, (self.start_button.x, self.start_button.y))
        self.canvas.blit(quit_text, (self.quit_button.x, self.quit_button.y))
    
    def go(self):
        running = True 
        # while running, the initalized window and create_interface_buttons def statements run first 
        while running: 
            self.init_window()
            self.create_interface_buttons()
            pygame.display.update()
            for event in pygame.event.get(): 
                # if you quit the screen, everything exits/quits
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()   
                # if you press the start button the powers_screen.py runs
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.start_button.collidepoint(event.pos):
                        new_screen = powers_screen.Display()
                        new_screen.go()
                    # if you press the provided quit button, you are exited out of the game 
                    if self.quit_button.collidepoint(event.pos): 
                        pygame.quit()
                        sys.exit()
            pygame.display.update

#main runs the class Display above 
def main():
    my_display = Display()
    my_display.go()

# runs the main function above 
if __name__ == "__main__":
    main()