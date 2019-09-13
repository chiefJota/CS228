import pickle
import numpy
import os
from pygameWindow_Del03 import PYGAME_WINDOW
import constants as constants
import time


class READER:
    def __init__(self):

        self.pygameWindow_Del03 = PYGAME_WINDOW()
        
        self.readData()

##########################################
    def readData(self):
         path, dirs, files = next(os.walk('userData'))
         self.numGestures = len(files)
##########################################
    def Print_Gestures(self):
        i = 0
        fileNum = str(i)
        for i in range(self.numGestures):
            pickleIn = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/gesture"+fileNum+".p", "rb", 0)
            gestureData = pickle.load(pickleIn)
            print(gestureData)
            
##########################################
    def Draw_Gestures(self):
        #create an infinite loop
        while True:
            self.Draw_Each_Gesture_Once()

##########################################
    def Draw_Each_Gesture_Once(self):

        xBase = 0 
        yBase = 0 
        zBase = 0
        xTip = 0
        yTip = 0
        zTip = 0

        for fileNum in range(self.numGestures):

            #call Draw_Gesture
            self.pygameWindow_Del03.Prepare()
            #i = 0
            #print(gestureData)
            g = str(fileNum)
            pickleIn = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/gesture"+g+".p", "rb", 0)
            gestureData = pickle.load(pickleIn)
            #right after loading gestureData
            for i in range(0, 5):
                for j in range(0, 4):
                    xBase = gestureData[i,j,0] 
                    yBase = gestureData[i,j,1]
                    zBase = gestureData[i,j,2] 
                    xTip = gestureData[i,j,3] 
                    yTip = gestureData[i,j,4] 
                    zTip = gestureData[i,j,5]  

                    currentBone = [xBase,yBase,zBase,xTip,yTip,zTip]
                    xBaseNotYetScaled = currentBone[0]
                    yBaseNotYetScaled = currentBone[1]
                    xTipNotYetScaled = currentBone[3]
                    yTipNotYetScaled = currentBone[4]

                    zBaseNotYetScaled = currentBone[2]
                    zTipNotYetScaled = currentBone[5]


                    xBase = self.Scale(xBaseNotYetScaled, constants.xMin, constants.xMax, 0, constants.pygameWindowWidth)
                    yBase = self.Scale(yBaseNotYetScaled, constants.yMin, constants.yMax, constants.pygameWindowDepth, 0)
                    xTip = self.Scale(xTipNotYetScaled, constants.xMin, constants.xMax, 0, constants.pygameWindowWidth)
                    yTip = self.Scale(yTipNotYetScaled, constants.yMin, constants.yMax, constants.pygameWindowDepth, 0)

                    zBase = self.Scale(zBaseNotYetScaled, constants.xMin, constants.xMax, 0, constants.pygameWindowWidth)
                    zTip = self.Scale(zTipNotYetScaled, constants.yMin, constants.yMax, 0, constants.pygameWindowDepth)

                    self.pygameWindow_Del03.Draw_Line((0, 0, 255), xBase, zBase, xTip, zTip, 2)

            self.pygameWindow_Del03.Reveal()
            time.sleep(0.1)
##########################################
    def Draw_Gesture(self, curGesture):
        pass
       

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



