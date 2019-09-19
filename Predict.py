from knn import KNN
import matplotlib.pyplot as plt
import numpy as np

###############################################
#create an instance of the kNN class
knn = KNN()

knn.Load_Dataset('iris.csv')

#first feature of flower
x = knn.data[:,0:1]
#second feature of flower
y = knn.data[:,1:2]

#Have to reshape because the scatter function
#doesn't like arrays the same size as x and y???
targ = knn.target
reshape = np.reshape(targ, (150, 1))

# plt.figure()
# plt.scatter(x,y, c=reshape)
# plt.show()

###############################################
#start at row 0 and skip every other row  of second and third
trainX = knn.data[::2,1:3]
trainy = knn.target[::2]
#get the first and second columns of trainX
x = trainX[:,0:1]
y = trainX[:,1:2]
#need to reshape it again
train_y = np.reshape(trainy, (75, 1))

#start at row "1" and take every 2 rows
#after
testX = knn.data[1::2,1:3]
testy = knn.target[1::2]



#set the k value
knn.Use_K_Of(15)
knn.Fit(trainX, trainy)

for i in range(0, 75):
    actualClass = testy[i]
    prediction = knn.Predict(testX[i,0:2])
    #print(testy[2])
    #print(testX[74,0:2])
    #print(actualClass, prediction)
#print(numRight)

xOdd = testX[:,0:1]
yOdd = testX[:,1:2]

test_y = np.reshape(testy, (75, 1))

###############################################
colors = np.zeros((3,3), dtype='f')
colors[0,:] = [1, 0.5, 0.5]
colors[1,:] = [0.5, 1, 0.5]
colors[2,:] = [0.5, 0.5, 1]

plt.figure()
#distinguish between training and testing points
[numItems, numFeatures] = knn.data.shape
for i in range(0, numItems/2):
     itemClass = int(trainy[i])
     currColor = colors[itemClass,:]
     plt.scatter(trainX[i, 0], trainX[i, 1],edgecolor = 'black', facecolor = currColor, s=50, lw=2)

numRight = 0
for i in range(0, numItems/2):
     itemClass = int(testy[i])
     currColor = colors[itemClass,:]
     prediction = int(knn.Predict(testX[i,:]))
     if(prediction == itemClass):
         numRight+=1
     edgeColor = colors[prediction,:]
     plt.scatter(testX[i, 0], testX[i, 1], edgecolor = edgeColor, facecolor = currColor, s=50, lw=2)  
print(numRight)

testItems = float(len(testX))
percentage = float(numRight/testItems) * 100
print(percentage)

plt.show()
