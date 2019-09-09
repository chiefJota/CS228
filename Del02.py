##########################################
import sys
sys.path.insert(0, '..')
import Leap
from pygameWindow import PYGAME_WINDOW
#import random
import constants as constants

pygameWindow = PYGAME_WINDOW()

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

##########################################
def Handle_Vector_From_Leap(v):
    global x, y
    global xMin, xMax, yMin, yMax

    x = int(v[0])
    #change to this when you get the scaling correct
    #and to have it facing the correct direction
    #y = int(v[1])
    y = int(v[2])

    scaleX = Scale(x, xMin, xMax, 0, constants.pygameWindowWidth)
    scaleY = Scale(y, yMin, yMax, 0, constants.pygameWindowDepth)

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
    base = bone.prev_joint
    tip = bone.next_joint
    #xBase = int(base[0])
    #yBase = int(base[1])
    # xTip = int(tip[0])
    # yTip = int(tip[1])
    baseInfo = Handle_Vector_From_Leap(base)
    tipInfo = Handle_Vector_From_Leap(tip)

    #change to this eventually so that hand is drawn correctly
    pygameWindow.Draw_Black_Line(baseInfo[0], baseInfo[1], tipInfo[0], tipInfo[1], width)
   
##########################################
def Handle_Finger(finger):
    global width
    for b in range(0, 4):
        bone = finger.bone(b)
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

##########################################
def Handle_Frame(frame):

    global x, y
    global xMin, xMax, yMin, yMax
    hand = frame.hands[0]
    fingers = hand.fingers
    #print(str(len(fingers)))
    for finger in fingers:
        #print right after assignment 
        #print(finger)
        Handle_Finger(finger)        
    #exit()
        
    # indexFingerList = fingers.finger_type(1)
    # indexFinger = indexFingerList[0]
    # distalPhalanx = indexFinger.bone(3)
    # tip = distalPhalanx.next_joint
    # x = int(tip[0])
    # y = int(tip[1])
    # #print(tip)

    
    # print(xMin)
    # print(xMax)
    # print(yMin)
    # print(yMax)

    #print(hand)

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

while True:

    pygameWindow.Prepare()

    # #sandwich this between prepare and reveal
    frame = controller.frame()
    
    # ##want to change the position of the dot only when you hover
    # ##your hand over the device
    # #hands = frame.hands[0]
    handlist = frame.hands

    # #if the list is not empty
    if(handlist > 0):
        Handle_Frame(frame)
    #     #print("Hand detected")
    #     #print(len(handlist))

    #     #call scale twice after Handle_Frame
    #     #switch origin for y to move correctly with finger
    #     pygameX = Scale(x, xMin, xMax, 0, constants.pygameWindowWidth)
    #     pygameY = Scale(y, yMin, yMax, constants.pygameWindowDepth, 0)
    #     print( x, pygameX)
    #     print( y, pygameY)


    # #call this right after conditional statement
    # pygameWindow.Draw_Black_Circle(pygameX, pygameY)

    #Perturb_Circle_Position()
    pygameWindow.Reveal()
