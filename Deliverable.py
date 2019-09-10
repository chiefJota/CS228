import sys
sys.path.insert(0, '..')
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW
import constants as constants


class DELIVERABLE:
    def __init__(self):

        self.pygameWindow_Del03 = PYGAME_WINDOW()

        self.controller = Leap.Controller()

        #"global" x and y
        self.x = 0
        self.y = 0

        #"global" min and max dimensions of windowsize
        self.xMin = -175.0
        self.xMax = 175.0
        self.yMin = -175.0
        self.yMax = 175.0

        self.width = 5

        self.color = (0, 0, 0) 

        self.previousNumberOfHands = 0
        self.currentNumberOfhands = 0
##########################################
    def Handle_Vector_From_Leap(self, v):

        self.x = int(v[0])
        #change to this when you get the scaling correct
        #and to have it facing the correct direction
        #y = int(v[1])
        self.y = int(v[2])

        scaleX = self.Scale(self.x, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
        scaleY = self.Scale(self.y, self.yMin, self.yMax, 0, constants.pygameWindowDepth)

        if(self.x < self.xMin):
            self.xMin = self.x
        if(self.x > self.xMax):
            self.xMax = self.x

        if(self.y < self.yMin):
            self.yMin = self.y
        if(self.y > self.yMax):
            self.yMax = self.y

        #Scale the two values like you did previously
        return scaleX, scaleY
    

##########################################
    def Handle_Bone(self, bone):
        #global width
        base = bone.prev_joint
        tip = bone.next_joint
        #xBase = int(base[0])
        #yBase = int(base[1])
        # xTip = int(tip[0])
        # yTip = int(tip[1])
        baseInfo = self.Handle_Vector_From_Leap(base)
        tipInfo = self.Handle_Vector_From_Leap(tip)

        #gets the number of hands
        numHands = len(self.currentNumberOfhands)

        if(numHands == 1):
            self.color = (0, 255, 0)
        elif(numHands == 2):
            self.color = (255, 0, 0)

        self.pygameWindow_Del03.Draw_Line(self.color, baseInfo[0], baseInfo[1], tipInfo[0], tipInfo[1], self.width)
    
##########################################
    def Handle_Finger(self, finger):
        # global width
        for b in range(0, 4):
            bone = finger.bone(b)
            if(b == 0):
                self.width = 5
            elif(b == 1):
                self.width = 4
            elif(b == 2):
                self.width = 3
            elif(b == 3):
               self.width  = 2
            elif(b == 4):
                self.width  = 1 
            self.Handle_Bone(bone)

##########################################
    def Handle_Frame(self, frame):

        hand = frame.hands[0]
        #print(hand)
        fingers = hand.fingers
        #print(str(len(fingers)))
        for finger in fingers:
            #print right after assignment 
            #print(finger)
            self.Handle_Finger(finger)   

        if(self.Recording_Is_Ending()):
            print("recording is ending.")     
    
##########################################
    #arg 1 should lie within a range defined by args 2 and 3.
    #and should be scaled so that it lies within the new range
    #defined by args 4 and 5
    def Scale(self, fingerPosition, leapStart, leapEnd, appStart, appEnd):

        deviceRange = leapEnd - leapStart

        #xMin == xMax and yMin == yMax
        if(deviceRange == 0):
            curPosition = appStart

        else:
            appRange = appEnd - appStart
            curPosition = (((fingerPosition - leapStart) * appRange)/deviceRange) + appStart
        return int(curPosition)


##########################################
    def Run_Forever(self):
        while True:
            self.Run_Once()
            

##########################################
    def Run_Once(self):
        self.pygameWindow_Del03.Prepare()
        #capture a frame
        frame = self.controller.frame()
        #stores the current number of hands in the frame
        self.currentNumberOfhands = frame.hands

        #if the curr num of hands is not 0
        if(self.currentNumberOfhands > 0):
            #print(len(self.numberOfHands))
            self.Handle_Frame(frame)
        
        #as its about to exit and iteration store curNumHands in prevNumHands
        self.previousNumberOfHands = len(self.currentNumberOfhands)

        self.pygameWindow_Del03.Reveal()

       

    def Recording_Is_Ending(self):
        #should return true when there is one hand over the device
        #but there was two hands over it in the previous iteration
        numHands = len(self.currentNumberOfhands)
        #prevNumHands = len(self.previousNumberOfHands)

        if(numHands == 1 and self.previousNumberOfHands == 2):
            return True
        else:
            return False
