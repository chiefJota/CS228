import pickle
import numpy
import os
from pygameWindow import PYGAME_WINDOW


class READER:
    def __init__(self):

        self.pygameWindow = PYGAME_WINDOW()
        
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
            self.pygameWindow.Prepare()
            #print(gestureData)
            pickleIn = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/gesture"+str(fileNum)+".p", "rb", 0)
            gestureData = pickle.load(pickleIn)
            #right after loading gestureData
            for i in range(4):
                for j in range(3):
                    gestureData[i,j,0] = xBase
                    gestureData[i,j,1] = yBase
                    gestureData[i,j,2] = zBase
                    gestureData[i,j,3] = xTip
                    gestureData[i,j,4] = yTip
                    gestureData[i,j,5] = zTip

            


            self.pygameWindow.Reveal()
            self.Draw_Gesture(i)
##########################################
    def Draw_Gesture(self, curGesture):
       pass


