import pickle
import numpy

class READER:
    def __init__(self):
        pickleIn = open("/Users/Chief/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/CS228/userData/gesture.p", "rb", 0)
        gestureData = pickle.load(pickleIn)

        print(gestureData)