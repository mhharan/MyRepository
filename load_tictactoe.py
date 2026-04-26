# Check the versions of libraries
import random, os, time
import numpy as np

from os import system
from time import sleep

import network

training_data=[None]*20
test_data=[None]*6

a = np.array(([0],[0],[0],[0],[0],[0]),dtype=np.float32)
b = np.array(([0],[0],[0]))
training_data[0]=tuple((a,b))

a = np.array(([0],[0],[0],[0],[1],[0]),dtype=np.float32)
b = np.array(([0],[0],[1]))
training_data[1]=tuple((a,b))

a = np.array(([0],[0],[0],[0],[0],[1]),dtype=np.float32)
b = np.array(([0],[0],[1]))
training_data[2]=tuple((a,b))


a = np.array(([0],[0],[0],[0],[1],[1]),dtype=np.float32)
b = np.array(([0],[0],[1]))
training_data[3]=tuple((a,b))

a = np.array(([0],[0],[0],[1],[0],[0]),dtype=np.float32)
b = np.array(([0],[1],[0]))
training_data[4]=tuple((a,b))

a = np.array(([0],[0],[1],[0],[0],[0]),dtype=np.float32)
b = np.array(([0],[1],[0]))
training_data[5]=tuple((a,b))

a = np.array(([0],[0],[1],[1],[0],[0]),dtype=np.float32)
b = np.array(([0],[1],[0]))
training_data[6]=tuple((a,b))

a = np.array(([0],[1],[0],[0],[0],[0]),dtype=np.float32)
b = np.array(([1],[0],[0]))
training_data[7]=tuple((a,b))

a = np.array(([1],[0],[0],[0],[0],[0]),dtype=np.float32)
b = np.array(([1],[0],[0]))
training_data[8]=tuple((a,b))

a = np.array(([1],[1],[0],[0],[0],[0]),dtype=np.float32)
b = np.array(([1],[0],[0]))
training_data[9]=tuple((a,b))

a = np.array(([0],[0],[0],[0],[0],[0]),dtype=np.float32)
b = np.array(([0],[0],[0]))
training_data[10]=tuple((a,b))

a = np.array(([0],[0],[0],[0],[1],[0]),dtype=np.float32)
b = np.array(([0],[0],[1]))
training_data[11]=tuple((a,b))

a = np.array(([0],[0],[0],[0],[0],[1]),dtype=np.float32)
b = np.array(([0],[0],[1]))
training_data[12]=tuple((a,b))


a = np.array(([0],[0],[0],[0],[1],[1]),dtype=np.float32)
b = np.array(([0],[0],[1]))
training_data[13]=tuple((a,b))

a = np.array(([0],[0],[0],[1],[0],[0]),dtype=np.float32)
b = np.array(([0],[1],[0]))
training_data[14]=tuple((a,b))

a = np.array(([0],[0],[1],[0],[0],[0]),dtype=np.float32)
b = np.array(([0],[1],[0]))
training_data[15]=tuple((a,b))

a = np.array(([0],[0],[1],[1],[0],[0]),dtype=np.float32)
b = np.array(([0],[1],[0]))
training_data[16]=tuple((a,b))

a = np.array(([0],[1],[0],[0],[0],[0]),dtype=np.float32)
b = np.array(([1],[0],[0]))
training_data[17]=tuple((a,b))

a = np.array(([1],[0],[0],[0],[0],[0]),dtype=np.float32)
b = np.array(([1],[0],[0]))
training_data[18]=tuple((a,b))

a = np.array(([1],[1],[0],[0],[0],[0]),dtype=np.float32)
b = np.array(([1],[0],[0]))
training_data[19]=tuple((a,b))

a = np.array(([0],[0],[0],[0],[1],[0]),dtype=np.float32)
test_data[0]=tuple((a,2))

a = np.array(([0],[0],[1],[1],[0],[0]),dtype=np.float32)
test_data[1]=tuple((a,1))

a = np.array(([1],[1],[0],[0],[0],[0]),dtype=np.float32)
test_data[2]=tuple((a,0))

a = np.array(([0],[0],[0],[0],[0],[1]),dtype=np.float32)
test_data[3]=tuple((a,2))

a = np.array(([1],[1],[0],[0],[0],[0]),dtype=np.float32)
test_data[4]=tuple((a,0))

a = np.array(([0],[0],[0],[0],[1],[1]),dtype=np.float32)
test_data[5]=tuple((a,2))

#print(training_data)
#print(test_data)
net = network.Network([6, 30, 3])
net.SGD(training_data, 100, 10, .25, test_data=test_data)

# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),(0)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),(0)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),(0)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),(0)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),(0)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),(0)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),(0)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(0)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(0)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(0)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(0)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(0)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(0)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(0)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(0)] 
# training_data[-1] =[(0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(1)] 
# training_data[-1] =[(1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1),(1)] 
# training_data[-1] =[(1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1),(1)] 
# training_data[-1] =[(1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1),(1)] 
# training_data[-1] =[(1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1),(1)] 
# training_data[-1] =[(1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1),(1)] 
# training_data[-1] =[(1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1),(1)] 
# training_data[-1] =[(1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0),(1)] 
# training_data[-1] =[(0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),(1)] 
# training_data[-1] =[(1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0),(1)] 
# training_data[-1] =[(1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0),(1)] 
# training_data[-1] =[(1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0),(1)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0),(1)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0),(1)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0),(1)] 
# training_data[-1] =[(1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0),(1)] 
# training_data[-1] =[(0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1),(1)] 
# training_data[-1] =[(0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1),(1)] 
# training_data[-1] =[(0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1),(1)] 
# training_data[-1] =[(0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1),(1)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1),(1)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1),(1)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1),(1)] 
# training_data[-1] =[(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0),(1)] 

#print(training_data)
