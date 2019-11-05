import pygame
from pygameWindow_Del03 import PYGAME_WINDOW
pygameWindow = PYGAME_WINDOW()
##########################################
def draw_startUpImage():
    global startImage
    startImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/startImage.png")
    pygameWindow.screen.blit(startImage, (675, 175))

########################################## 
def draw_leftImage():
    LeftImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/left.png")
    pygameWindow.screen.blit(LeftImage, (675, 175))

########################################## 
def draw_rightImage():
    rightImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/right.png")
    pygameWindow.screen.blit(rightImage, (675, 175))

########################################## 
def draw_upImage():
    upImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/up.png")
    pygameWindow.screen.blit(upImage, (675, 175))

########################################## 
def draw_downImage():
    downImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/down.png")
    pygameWindow.screen.blit(downImage, (675, 175))

########################################## 
def draw_leftUpImage():
    leftUpImage = pygame.image.load("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/upLeft.png")
    pygameWindow.screen.blit(leftUpImage, (675, 175))
    
########################################## 
def draw_rightUpImage():
    upRightImage = pygame.image.load("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/upRight.png")
    pygameWindow.screen.blit(upRightImage, (675, 175))
   
########################################## 
def draw_rightDownImage():
    rightDownImage = pygame.image.load("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/downRight.png")
    pygameWindow.screen.blit(rightDownImage, (675, 175))
  
########################################## 
def draw_leftDownImage():
    leftDownImage = pygame.image.load("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/gestureDirections/downLeft.png")
    pygameWindow.screen.blit(leftDownImage, (675, 175))
    
