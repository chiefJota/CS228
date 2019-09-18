from knn import KNN
import matplotlib.pyplot as plt
import numpy as np

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

#contains even number rows and first two columns
trainX = knn.data[::2,0:2]
trainy = knn.target[::2]

#get the first and second columns of trainX
x = trainX[:,0:1]
y = trainX[:,1:2]

#need to reshape it again
train_y = np.reshape(trainy, (75, 1))

#start at row "1" and take every 2 rows
#after
testX = knn.data[1::2,0:2]
testy = knn.target[1::2]

xOdd = testX[:,0:1]
yOdd = testX[:,1:2]

test_y = np.reshape(testy, (75, 1))

#print(xOdd)
print(yOdd)

plt.figure()
#distinguish between training and testing points
plt.scatter(x,y,c=train_y, edgecolors='black')
plt.scatter(xOdd, yOdd,c=test_y)
plt.show()
