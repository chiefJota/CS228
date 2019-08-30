import sys
sys.path.insert(0, '..')
import Leap
from pygameWindow import PYGAME_WINDOW
#import random
#import constants as constants

pygameWindow = PYGAME_WINDOW()

x = 450
y = 450

#def Perturb_Circle_Position():

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
controller = Leap.Controller()

def Handle_Frame(frame):
    global x, y
    hand = frame.hands[0]
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(1)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(3)
    tip = distalPhalanx.next_joint
    x = int(tip[0])
    y = int(tip[1])
    print(tip)
    #print(hand)

while True:
    pygameWindow.Prepare()
    pygameWindow.Draw_Black_Circle(x, y)
    frame = controller.frame()

#    Perturb_Circle_Position()
    pygameWindow.Reveal()

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
