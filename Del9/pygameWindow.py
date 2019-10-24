import pygame
import constants as constants
class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth))



    def Prepare(self):
        pygame.event.get()
        self.screen.fill((255, 255, 255))


    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Circle(self, x, y):
        pygame.draw.circle(self.screen, (0, 0, 0), [x, y], 15)

    def Draw_Black_Line(self, xBase, yBase, xTip, yTip, width):
        pygame.draw.line(self.screen, (0, 0, 0), (xBase, yBase), (xTip, yTip), width)

    def Draw_Black_Panels(self, color, xStart, yStart, xEnd, yEnd, width):
         pygame.draw.rect(self.screen,(0,0,0), (xStart, yStart, xEnd, yEnd), width)