import pygame
import constants as constants
class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowHeight))


    def Prepare(self):
        self.screen.fill([255, 255, 255])

    def Reveal(self):
        pygame.display.update()
