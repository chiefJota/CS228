import numpy as np 
import pickle 
from knn import KNN

train1 = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/trainM.p", "rb", 0)
trainM = pickle.load(train1)
# print(trainM)
# print(trainM.shape)
train2 = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/trainN.p", "rb", 0)
trainN = pickle.load(train2)
# print(trainN)
# print(trainN.shape)
test1 = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/testM.p", "rb", 0)
testM = pickle.load(test1)
#print(testM)
#print(testM.shape)
test2 = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/testN.p", "rb", 0)
testN = pickle.load(test2)
#print(testN)
#print(testN.shape)
##########################################
def centerData(X):
    allXCoordinates = X[:,:,0,:]
    meanValue = allXCoordinates.mean()
    X[:,:,0,:] = allXCoordinates-meanValue

    allYCoordinates = X[:,:,1,:]
    meanYValue = allYCoordinates.mean()
    X[:,:,1,:] = allYCoordinates-meanYValue
    
    allZCoordinates = X[:,:,2,:]
    meanZValue = allZCoordinates.mean()
    X[:,:,2,:] = allZCoordinates-meanZValue
    #print(X[:,:,2,:].mean())
    
    return X  

##########################################  
def ReduceData(X):
    #first call cuts out (the proximal phalange)
    X = np.delete(X, 1, 1)
    #second call cuts out (the intermediate phalange)
    X = np.delete(X, 1, 1)
    #delete the first instance along the third dimension of X 3 times
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)

    return X

##########################################   
def ReshapeData(set1, set2):
    X = np.zeros((2000, 5*2*3), dtype="f")
    y = np.zeros(2000)
    for row in range(0, 1000):
        y[row] = 1
        y[row+1000] = 2
        col = 0
        for finger in range(0,5):
            for joint in range (0,2):
                for coords in range(0,3):
                    X[row, col] = set1[finger,joint,coords,row]
                    X[row+1000, col] = set2[finger,joint,coords,row]
                    col = col + 1
    return X, y
##########################################   
trainM = ReduceData(trainM)
trainN = ReduceData(trainN)
testM = ReduceData(testM)
testN = ReduceData(testN)

centerData(trainM)
centerData(trainN)
centerData(testM)
centerData(testN)


trainX, trainy = ReshapeData(trainM, trainN)
testX, testy = ReshapeData(testM, testN)

#create an instance of knn
knn = KNN()

#set k value and fit the data
knn.Use_K_Of(15)
knn.Fit(trainX, trainy)

numRight = 0
for row in range(0, 2000):
    prediction = knn.Predict(testX[row])
    actualClass = testy[row]
    if(prediction == actualClass):
        numRight+=1
print(numRight)

vecY = float(len(trainy))
percentage = float(numRight/vecY) * 100
print(percentage)
##########################################   


 