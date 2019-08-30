import sys
sys.path.insert(0, '..')
import Leap
from pygameWindow import PYGAME_WINDOW
#import random
#import constants as constants

pygameWindow = PYGAME_WINDOW()

#"global" x and y
x = 0
y = 0

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

##########################################
def Handle_Frame(frame):

    global x, y
    global xMin, xMax, yMin, yMax
    hand = frame.hands[0]
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(1)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(3)
    tip = distalPhalanx.next_joint
    x = int(tip[0])
    y = int(tip[1])
    print(tip)

    if(x < xMin):
        xMin = x
    if(x > xMax):
        xMax = x

    if(y < yMin):
        yMin = y
    if(y > yMax):
        yMax = y
    print(xMin)
    print(xMax)
    print(yMin)
    print(yMax)

    #print(hand)

##########################################
def Scale(x1, x2, x3, x4, x5):
    



##########################################

controller = Leap.Controller()

while True:
    pygameWindow.Prepare()
    #sandwich this between prepare and reveal
    frame = controller.frame()

    ##want to change the position of the dot only when you hover
    ##your hand over the device
    #hands = frame.hands[0]
    handlist = frame.hands
    for hands in handlist:
        #if the list is not empty
        if(handlist > 0):
            Handle_Frame(frame)
            #print("Hand detected")
            #print(len(handlist))
    #call this right after conditional statement
    pygameWindow.Draw_Black_Circle(x, y)

    #Perturb_Circle_Position()
    pygameWindow.Reveal()

##########################################
#def Perturb_Circle_Position():
    #global x, y
#    fourSidedDieRoll = random.randint(1,4)

    #decrease horizontal position by 1
#    if(fourSidedDieRoll == 1):
#        x = x-constants.circleVelocity
    #increase horizontal position by 1
#    elif(fourSidedDieRoll == 2):
#        x = x+constants.circleVelocity
    #decrease vertical position by 1
#    elif(fourSidedDieRoll == 3):
#        y = y-constants.circleVelocity
    #increase vertical position by 1
#    else:
#        y = y+constants.circleVelocity

#print(pygameWindow)
