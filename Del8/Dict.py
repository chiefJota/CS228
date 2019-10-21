import pickle
import pygame
import sys
sys.path.insert(0, '../..')
import Leap
from pygameWindow import PYGAME_WINDOW
import constants as constants

import numpy as np
import handDirection
import random
import time

##########################################
def login():
    global database
    global userRecord
    #load database from pickled file
    database = pickle.load(open('/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del8/userData/database.p','rb'))

    userName = raw_input("Please enter your name: ")
    #returning user
    if userName in database:
        #welcome back kid
        print("welcome back " + userName + ".")  
        #get number of logins associated with the user
        database[userName]['logins']+=1
    else:
        #set value for key
        database[userName] = {'logins' : 1}
        
        print("welcome " + userName + ".")  
        
    #print(database)
    #make dictionary to hold gesture info
    userRecord = database[userName]
    print(database)
##########################################

#prints this: {'logins': 1, 'digit3attempted': 1}

##########################################
login()

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
digitPresented = " "
framesGoneBy = 0

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
    global framesGoneBy
    #if no hands are detected
    if(not HandOverDevice(frame, handlist)):
        programState = 0
        framesGoneBy = 0

########################################## 
#Now, if the users hand is centered, pick one of the 10 ASL numbers at random and show it
# to the user in the upper right panel. Also, show an image of the ASL gesture corresponding
# to this digit in the lower right panel so the user knows what to do
def HandleState2(frame, handlist):
    global programState
    global framesGoneBy
    displayASL()   
    if(not HandOverDevice(frame, handlist)):
        programState = 0
        framesGoneBy = 0

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
    global digitPresented
    global userRecord
    global aslDigit
     
    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 32)
    
    if sucess == False:
        #choose random aslNum to gesture
        aslNum = random.randint(0, 9)
    
        if aslNum == 0:
            if('digit0presented' in userRecord):
                userRecord['digit0presented'] = userRecord['digit0presented'] + 1
            else:
                userRecord['digit0presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit0presented']), True, (0, 0, 0))
            num = '0'

        if aslNum == 1:
            if('digit1presented' in userRecord):
                userRecord['digit1presented'] = userRecord['digit1presented'] + 1
            else:
                userRecord['digit1presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit1presented']), True, (0, 0, 0))
            num = '1'

        if aslNum== 2:
            if('digit2presented' in userRecord):
                userRecord['digit2presented'] = userRecord['digit2presented'] + 1
            else:
                userRecord['digit2presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit2presented']), True, (0, 0, 0))
            num = '2'

        if aslNum == 3:
            if('digit3presented' in userRecord):
                userRecord['digit3presented'] = userRecord['digit3presented'] + 1
            else:
                userRecord['digit3presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit3presented']), True, (0, 0, 0))
            num = '3'
        if aslNum == 4:
            if('digit4presented' in userRecord):
                userRecord['digit4presented'] = userRecord['digit4presented'] + 1
                
            else:
                userRecord['digit4presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit4presented']), True, (0, 0, 0))
            num = '4'

        if aslNum == 5:
            if('digit5presented' in userRecord):
                userRecord['digit5presented'] = userRecord['digit5presented'] + 1
            else:
                userRecord['digit5presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit5presented']), True, (0, 0, 0))
            num = '5'

        if aslNum== 6:
            if('digit6presented' in userRecord):
                userRecord['digit6presented'] = userRecord['digit6presented'] + 1
            else:
                userRecord['digit6presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit6presented']), True, (0, 0, 0))
            num = '6'

        if aslNum== 7:
            if('digit7presented' in userRecord):
                userRecord['digit7presented'] = userRecord['digit7presented'] + 1
            else:
                userRecord['digit7presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit7presented']), True, (0, 0, 0))
            num = '7'

        if aslNum == 8:
            if('digit8presented' in userRecord):
                userRecord['digit8presented'] = userRecord['digit8presented'] + 1
            else:
                userRecord['digit8presented'] = 1
            aslDigit = font.render("Times Presented: " + str(userRecord['digit8presented']), True, (0, 0, 0))
            num = '8'

        if aslNum == 9:
            if('digit9presented' in userRecord):
                userRecord['digit9presented'] = userRecord['digit9presented'] + 1
            else:
                userRecord['digit9presented'] = 1
                aslDigit = font.render("Times Presented: " + str(userRecord['digit9presented']), True, (0, 0, 0))
            num = '9'
             
    sucess = True
    pygameWindow.screen.blit(aslDigit,(175,750))  
    daNumba = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/ASLNUMS/"+num+".png")
    pygameWindow.screen.blit(daNumba, (750, 175))
    aslSign = pygame.image.load("/Users/chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del7/ASLNUMS/asl"+num+".png")
    pygameWindow.screen.blit(aslSign, (675, 625))
    correctGesture(aslNum)
#############################################   
def correctGesture(aslNum):
    global programState
    global framesCorrect
    global sucess
    global predictedClass
    global framesGoneBy
    #check to see if the predictedNum is matching
    #the aslNum
    predictedClass = clf.Predict(testData)
   # print(predictedClass)
    if(predictedClass == aslNum):
        framesCorrect+=1
        framesGoneBy+=1
        print(framesGoneBy)
       # print(framesCorrect)
    if(predictedClass != aslNum):
        framesGoneBy+=1
        framesCorrect = 0
        print(framesGoneBy)
        programState = 2
    if(framesGoneBy >= 35):
        pickle.dump(database, open('userData/database.p','wb'))
        framesGoneBy = 0
        programState = 2
        sucess = False
        print(framesGoneBy)
    if(framesCorrect >= 10):
        #dump contents of dictionary in pickled file
        pickle.dump(database, open('userData/database.p','wb'))
        framesGoneBy = 0
        programState = 3
        print("success")
        print(framesGoneBy)

    
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
########################################## 
    
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


