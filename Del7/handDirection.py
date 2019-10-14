import pygame
import constants as constants
from pygameWindow import PYGAME_WINDOW
pygameWindow = PYGAME_WINDOW()
##########################################
def draw_startUpImage():
    global startImage
    startImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/HoverHandOverLEap.png")
    pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/8, 150))

########################################## 
def draw_leftImage():
    startImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/arrow pointing left.png")
    pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/4, 150))

########################################## 
def draw_rightImage():
    startImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/arrow right.png")
    pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/4, 150))

########################################## 
def draw_upImage():
    startImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/arrow pointing up.jpg")
    pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/4, 150))

########################################## 
def draw_downImage():
    startImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/arrow pointing down.png")
    pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/4, 150))

########################################## 
def draw_leftUpImage():
    # #startImage = pygame.image.load("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/HoverHandOverLEap.png")
    # pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/8, 150))
    pass
########################################## 
def draw_rightUpImage():
    # startImage = pygame.image.load("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/HoverHandOverLEap.png")
    # pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/8, 150))
    pass
########################################## 
def draw_rightDownImage():
    # startImage = pygame.image.load("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/HoverHandOverLEap.png")
    # pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/8, 150))
    pass
########################################## 
def draw_leftDownImage():
    # startImage = pygame.image.load("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/HoverHandOverLEap.png")
    # pygameWindow.screen.blit(startImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/8, 150))
    pass
