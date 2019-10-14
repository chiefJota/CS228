##########################################
import pygame
import sys
sys.path.insert(0, '../..')
import Leap
from pygameWindow import PYGAME_WINDOW
#import random
import constants as constants
import pickle
import numpy as np
import handDirection
import random
pygameWindow = PYGAME_WINDOW()

##########################################
clf = pickle.load(open('/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/userData/classifier.p', 'rb'))
testData = np.zeros((1,30),dtype ='f')
##########################################
#"global" x and y
x = 0
y = 0

#"global" min and max dimensions of windowsize
xMin = -175.0
xMax = 175.0
yMin = -175.0
yMax = 1.0

width = 5

k = 0

programState = 0
gloablNumFrames = 0
rightSign = 0
framesCorrect = 0
sucess = False

########################################## 
def handLocation(base):
    isCentered = True
    if (base[0] < -90) and (base[2] > 90):
        isCentered = False
        handDirection.draw_rightUpImage()
    elif (base[0] < -90) and (base[2] < 10):
        isCentered = False 
        handDirection.draw_rightDownImage()
    elif (base[0] > 90) and (base[2] > 90):
        isCentered = False 
        handDirection.draw_leftUpImage()
    elif (base[0] > 90) and (base[2] < 10):
        isCentered = False 
        handDirection.draw_leftDownImage()
    elif(base[0] < -100):
        isCentered = False 
        handDirection.draw_rightImage()
    elif(base[0] > 100):
        isCentered = False 
        handDirection.draw_leftImage()
    elif(base[2] > 100):
        isCentered = False 
        handDirection.draw_upImage()
    elif(base[2] < 0):
        isCentered = False 
        handDirection.draw_downImage()

    return isCentered

########################################## 
#If the user is able to keep their hand at the origin for a sufficiently long period of time
#(you decide what that time span should be), provide a visual cue to the user that they have
#succeeded.
def isHandCentered(hand, framesCentered):
    global programState
    #middle finger
    theBird = hand.fingers[2]
    #base of middle finger
    birdBase = theBird.bone(0)
    # center of middle finger base
    centerBird  = birdBase.prev_joint
    #check if its centered
    isCentered = handLocation(centerBird)

    #if the hand is centered
    if(isCentered == True):
        framesCentered+=1
    #hand isnt centered    
    if(isCentered == False):
        framesCentered = 0

    #the hand has been centered for 150 frames    
    if(framesCentered > 25):
        programState = 2
    
    if(framesCentered < 25):
        programState = 1
    
    return framesCentered

########################################## 
#hand is present
def HandleState0(frame, handslist):
    global programState
    handDirection.draw_startUpImage()
    #if hands are detected
    if(HandOverDevice(frame, handslist)):
        programState = 1

########################################## 
#hand is present but not centered
def HandleState1(frame, handlist):
    global programState
    #if no hands are detected
    if(not HandOverDevice(frame, handlist)):
        programState = 0
########################################## 
#whenever the hand is present and centered, 
# It should only show the virtual hand. 
#This may require you to add some if/then clauses
#to one or more of the three state-handling functions now.

#Now, if the users hand is centered, pick one of the 10 ASL numbers at random and show it
# to the user in the upper right panel. Also, show an image of the ASL gesture corresponding
# to this digit in the lower right panel so the user knows what to do
def HandleState2(frame, handlist):
    global programState
    displayASL()   
    if(not HandOverDevice(frame, handlist)):
        programState = 0

########################################## 
def HandleState3(frame, handlist):
    global programState, sucess
    sucessCount = 0
    #load the 
    while sucessCount < 500:
        successImage = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/ASLNUMS/aslSucess.jpg")
        successImage = pygameWindow.screen.blit(successImage, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/8, 150))
        sucessCount+=1
    sucess = False
    sucessCount = 0

    if(not HandOverDevice(frame, handlist)):
        programState = 0

########################################## 
def HandOverDevice(frame, handlist):
    global k
    # #if the list is not empty
    frame = frame
    handlist = handlist
    if(len(handlist) > 0):
        k = 0
        isHandOverDevice = True
    else:
        isHandOverDevice = False
    return isHandOverDevice
    
##########################################
def displayASL():
    global aslNum, num
    global sucess
     #choose random aslNum to gesture

    if sucess == False:
        aslNum = random.randrange(0, 10, 1)
        if aslNum == 0:
            num = '0'
        if aslNum == 1:
            num = '1'
        if aslNum== 2:
            num = '2'
        if aslNum == 3:
            num = '3'
        if aslNum == 4:
            num = '4'
        if aslNum == 5:
            num = '5'
        if aslNum== 6:
            num = '6'
        if aslNum== 7:
            num = '7'
        if aslNum == 8:
            num = '8'
        if aslNum == 9:
            num = '9'
    sucess = True
    daNumba = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/ASLNUMS/"+num+".png")
    pygameWindow.screen.blit(daNumba, (constants.pygameWindowWidth/2 + constants.pygameWindowWidth/6, 150))
    aslSign = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/ASLNUMS/asl"+num+".png")
    pygameWindow.screen.blit(aslSign, (constants.pygameWindowWidth / 2 + constants.pygameWindowWidth / 8, constants.pygameWindowDepth / 2 + constants.pygameWindowDepth / 8))
    correctGesture(aslNum)
#############################################   
def correctGesture(aslNum):
    global programState
    global framesCorrect
    global sucess
    global predictedClass
    #check to see if the predictedNum is matching
    #the aslNum
    predictedClass = clf.Predict(testData)
   # print(predictedClass)
    if(predictedClass == aslNum):
        framesCorrect+=1
        print(framesCorrect)
    if(predictedClass != aslNum):
        framesCorrect = 0
        programState = 2
    if(framesCorrect >= 10):
        programState = 3
        #Draw check mark or something
        print("success")
#############################################                     
def draw_panels():
    pygame.draw.line(pygameWindow.screen, (0,0,0),(constants.pygameWindowWidth/2, 0), (constants.pygameWindowWidth/2, constants.pygameWindowDepth), 2)
    pygame.draw.line(pygameWindow.screen, (0,0,0),(0, constants.pygameWindowDepth/2), (constants.pygameWindowWidth, constants.pygameWindowDepth/2), 2)

##########################################  
def CenterData(testData):
    allXCoordinates = testData[0,::3]
    meanXValue = allXCoordinates.mean()
    testData[0,::3] = allXCoordinates-meanXValue

    allYCoordinates = testData[0,1::3]
    meanYValue = allYCoordinates.mean()
    testData[0,1::3] = allYCoordinates-meanYValue
    
    allZCoordinates = testData[0,2::3]
    meanZValue = allZCoordinates.mean()
    testData[0,2::3] = allZCoordinates-meanZValue
    return testData  
    
##########################################
def Handle_Vector_From_Leap(v):
    global x, y
    global xMin, xMax, yMin, yMax

    x = int(v[0])
    #change to this when you get the scaling correct
    #and to have it facing the correct direction
    #y = int(v[1])
    y = int(v[2])

    scaleX = Scale(x, xMin, xMax, 0, constants.pygameWindowWidth/2)
    scaleY = Scale(y, yMin, yMax, 0, constants.pygameWindowDepth/2)

    if(x < xMin):
        xMin = x
    if(x > xMax):
        xMax = x

    if(y < yMin):
        yMin = y
    if(y > yMax):
        yMax = y

    #Scale the two values like you did previously
    return scaleX, scaleY
    

##########################################
def Handle_Bone(bone):
    global width
    global base, tip
    
    #xBase = int(base[0])
    #yBase = int(base[1])
    # xTip = int(tip[0])
    # yTip = int(tip[1])

    #Modifying the code to make sure that it workss
    global xTip,yTip,zTip
   # xTip = int(tip[0])
    #yTip = int(tip[1])
    #zTip = int(tip[2])

    baseInfo = Handle_Vector_From_Leap(base)
    tipInfo = Handle_Vector_From_Leap(tip)

    #change to this eventually so that hand is drawn correctly
    pygameWindow.Draw_Black_Line(baseInfo[0], baseInfo[1], tipInfo[0], tipInfo[1], width)
   
##########################################
def Handle_Finger(finger):
    global width
    global k 
    global base, tip
    global xTip,yTip,zTip
    global bone 
    global testData
    global predictedClass


    for b in range(0, 4):
        bone = finger.bone(b)

        base = bone.prev_joint
        tip  = bone.next_joint
        xTip = int(tip[0])
        yTip = int(tip[1])
        zTip = int(tip[2])

        if((b == 0 or (b == 3))):
            testData[0,k] = xTip
            testData[0, k+1] = yTip
            testData[0, k+2] = zTip
            k = k + 3

        if(b == 0):
            width = 5
        elif(b == 1):
            width = 4
        elif(b == 2):
            width = 3
        elif(b == 3):
            width  = 2
        elif(b == 4):
            width  = 1 
        Handle_Bone(bone)
    #print(testData)
    testData = CenterData(testData)
    

    # print(predictedClass)

##########################################
def Handle_Frame(frame, numFrames):
    global x, y
    global xMin, xMax, yMin, yMax
    global gloablNumFrames
    hand = frame.hands[0]
    fingers = hand.fingers
    #print(str(len(fingers)))
    for finger in fingers:
        #print right after assignment 
        #print(finger)
        Handle_Finger(finger)    

    if(numFrames == 0):
        count = isHandCentered(hand, numFrames)
        gloablNumFrames = count
    # Check that the hand is centered
    gloablNumFrames = isHandCentered(hand, gloablNumFrames)

   
##########################################
#arg 1 should lie within a range defined by args 2 and 3.
#and should be scaled so that it lies within the new range
#defined by args 4 and 5
def Scale(fingerPosition, leapStart, leapEnd, appStart, appEnd):
    deviceRange = leapEnd - leapStart

    #xMin == xMax and yMin == yMax
    if(deviceRange == 0):
        curPosition = appStart

    else:
        appRange = appEnd - appStart
        curPosition = (((fingerPosition - leapStart) * appRange)/deviceRange) + appStart
    return int(curPosition)
##########################################

controller = Leap.Controller()
numFrames = 0

while True:

    #prepare the window
    pygameWindow.Prepare()
    #draw the panels
    draw_panels()

    # #sandwich this between prepare and reveal
    frame = controller.frame()
    # #hands = frame.hands[0]
    handlist = frame.hands

    if(programState == 0):
        HandleState0(frame, handlist)
    if(programState == 1):
        HandleState1(frame, handlist)
    if(programState == 2):
        HandleState2(frame, handlist)
    if(programState == 3):
        HandleState3(frame, handlist)

    if(len(handlist) > 0):
        k = 0
        Handle_Frame(frame, numFrames)
        numFrames+=1
    #reveal window
    pygameWindow.Reveal()