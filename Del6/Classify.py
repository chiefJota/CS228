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
train0 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Childs_train0.p", "rb", 0))
test0 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Childs_test0.p", "rb", 0))

train3 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Liu_train3.p", "rb", 0))
test3 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Liu_test3.p", "rb", 0))

train4 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Ward_train4.p", "rb", 0))
test4 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Ward_test4.p", "rb", 0))

train5 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Peck_train5.p", "rb", 0))
test5 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Peck_test5.p", "rb", 0))

train6 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Boland_train6.p", "rb", 0))
test6 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Boland_test6.p", "rb", 0))

train7 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Rubin_train7.p", "rb", 0))
test7 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Rubin_test7.p", "rb", 0))

train8 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Mardis_train8.p", "rb", 0))
test8 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Mardis_test8.p", "rb", 0))

train9 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Lee_train9.p", "rb", 0))
test9 = pickle.load(open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/Del6/userData/Lee_test9.p", "rb", 0))
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
def ReshapeData(set1, set2, set3, set4, set5,set6, set7, set8, set9, set10):
    X = np.zeros((10000, 5*2*3), dtype="f")
    y = np.zeros(10000)
    for row in range(0, 1000):
        y[row] = 1
        y[row+1000] = 2
        y[row+2000] = 0
        y[row+3000] = 3
        y[row+4000] = 4
        y[row+5000] = 5
        y[row+6000] = 6
        y[row+7000] = 7
        y[row+8000] = 8
        y[row+9000] = 9
        
        col = 0
        for finger in range(0,5):
            for joint in range (0,2):
                for coords in range(0,3):
                    X[row, col] = set1[finger,joint,coords,row]
                    X[row+1000, col] = set2[finger,joint,coords,row]
                    X[row+2000, col] = set3[finger,joint,coords,row]
                    X[row+3000, col] = set4[finger, joint,coords,row]
                    X[row+4000, col] = set5[finger, joint,coords,row]
                    X[row+5000, col] = set6[finger, joint,coords,row]
                    X[row+6000, col] = set7[finger, joint,coords,row]
                    X[row+7000, col] = set8[finger, joint,coords,row]
                    X[row+8000, col] = set9[finger, joint,coords,row]
                    X[row+9000, col] = set10[finger, joint,coords,row]
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


train0 = ReduceData(train0)
test0 = ReduceData(test0)
train3 = ReduceData(train3)
test3 = ReduceData(test3)
train4 = ReduceData(train4)
test4 = ReduceData(test4)
train5 = ReduceData(train5)
test5 = ReduceData(test5)
train6 = ReduceData(train6)
test6 = ReduceData(test6)
train7 = ReduceData(train7)
test7 = ReduceData(test7)
train8 = ReduceData(train8)
test8  = ReduceData(test8)
train9 = ReduceData(train9)
test9 = ReduceData(test9)

centerData(train0)
centerData(test0)
centerData(train3)
centerData(test3)

centerData(train4)
centerData(test4)
centerData(train5)
centerData(test5)

centerData(train6)
centerData(test6)
centerData(train7)
centerData(test7)

centerData(train8)
centerData(test8)
centerData(train9)
centerData(test9)

trainX, trainy = ReshapeData(trainM, trainN, train0, train3, train4, train5, train6, train7, train8, train9)
testX, testy = ReshapeData(testM, testN, test0, test3, test4, test5, test6, test7, test8, test9)

#create an instance of knn
knn = KNN()

#set k value and fit the data
knn.Use_K_Of(15)
knn.Fit(trainX, trainy)

numRight = 0
for row in range(0, 10000):
    prediction = knn.Predict(testX[row])
    actualClass = testy[row]
    if(prediction == actualClass):
        numRight+=1
print(numRight)

vecY = float(len(trainy))
percentage = float(numRight/vecY) * 100
print(percentage)
##########################################   
pickle.dump(knn, open("userData/classifier.p", "wb"))

 