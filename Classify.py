import numpy as np 
import pickle 

train1 = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/train1.p", "rb", 0)
trainM = pickle.load(train1)
# print(trainM)
# print(trainM.shape)

train2 = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/train2.p", "rb", 0)
trainN = pickle.load(train2)
# print(trainN)
# print(trainN.shape)

test1 = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/test1.p", "rb", 0)
testM = pickle.load(test1)
#print(testM)
#print(testM.shape)

test2 = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/test2.p", "rb", 0)
testN = pickle.load(test2)
#print(testN)
#print(testN.shape)

def ReshapeData(set1, set2):
    X = np.zeros((2000, 5*4*6), dtype="f")
    y = np.zeros(2000)
    print(len(y))
    for row in range(0, 1000):
        y[row] = 1
        y[row+1000] = 2
        col = 0
        for finger in range(0,5):
            for joint in range (0,4):
                for coords in range(0,6):
                    X[row, col] = set1[finger,joint,coords,row]
                    X[row+1000, col] = set2[finger,joint,coords,row]
                    col = col + 1
    return X, y


trainX, trainy = ReshapeData(trainM, trainN)
testX, testy = ReshapeData(testM, testN)
# print(trainX)
# print(trainX.shape)
# print(trainy)
# print(trainy.shape)

# print(testX)
# print(testX.shape)
# print(testy)
# print(testy.shape)