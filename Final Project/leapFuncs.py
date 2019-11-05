
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

    #the hand has been centered for 25 frames    
    if(framesCentered > 10):
        programState = 2
    if(framesCentered < 10):
        programState = 1
    
    return framesCentered


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
    #Modifying the code to make sure that it workss
    global xTip,yTip,zTip
    #Change color if the user is signing correctly or inccorrectly
    global color
    global correctSign

    baseInfo = Handle_Vector_From_Leap(base)
    tipInfo = Handle_Vector_From_Leap(tip)

    if(correctSign == True):
        color = (0, 255, 0)
    elif(correctSign == False):
        color = (255,0,0)
    #change to this eventually so that hand is drawn correctly
    pygameWindow.Draw_Line(color, baseInfo[0], baseInfo[1], tipInfo[0], tipInfo[1], width)
   
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

    testData = CenterData(testData)
    

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


########################################## 