import numpy as np 
import pickle 

pickleIn = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/train1.p", "rb", 0)
gestureData = pickle.load(pickleIn)
print(gestureData.shape)