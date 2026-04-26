# Check the versions of libraries
import numpy as np, random, os

lr = 1 #learning rate
bias = 1 #value of bias
weights = [random.random(),random.random(),random.random()] #weights generated in a list (3 weights in total for 2 neurons and the bias)

	
def Perceptron(input1, input2, output) :
   outputP = input1*weights[0]+input2*weights[1]+bias*weights[2]
   
   if outputP > 0 : #activation function (here Heaviside)
      FinaloutputP = 1
   else :
      FinaloutputP = 0

   error = output-FinaloutputP
   weights[0] += error * input1 * lr
   weights[1] += error * input2 * lr
   weights[2] += error * bias * lr


# Teaching the Neural Network so that it build the Weights  
for i in range(1000) :
   Perceptron(1,1,1) #True or true
   Perceptron(1,0,0) #True or false
   Perceptron(0,1,0) #False or true
   Perceptron(0,0,0) #False or false

# Now see What it has learnt 
print("Type value of X and then Y")
x = int(input())
y = int(input())
outputP = x*weights[0] + y*weights[1] + bias*weights[2]
if outputP > 0 : #activation function
   FinaloutputP = 1
else :
   FinaloutputP = 0
print("Perceptron Output (w.x + b) for ", x, "or", y, "is : ", FinaloutputP)   

