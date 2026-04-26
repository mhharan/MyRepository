# Check the versions of libraries
import numpy, random, os

lr = 1 #learning rate
bias = 1 #value of bias
weights_5_neurons = [random.random(),random.random(),random.random(),random.random(),random.random(),random.random()] 

def ActivationFunction_5_neurons(input1, weights1, input2, weights2,input3, weights3, input4, weights4, input5, weights5, bias, weights6) :
   outputP = input1*weights1+input2*weights2+input3*weights3+input4*weights4+input5*weights5+bias*weights6

   if outputP > 0 : #activation function (here Heaviside)
      outputP = 1
   else :
      outputP = 0
	
   return outputP

def Perceptron_5_neurons(game_status_row1, game_status_row2, game_status_row3, game_status_across1, game_status_across2,game_status) :
   outputP = ActivationFunction_5_neurons(game_status_row1,weights_5_neurons[0],game_status_row2,weights_5_neurons[1],game_status_row3,weights_5_neurons[2],game_status_across1,weights_5_neurons[3],game_status_across2,weights_5_neurons[4],bias,weights_5_neurons[5])   
   
   error = game_status-outputP
   weights_5_neurons[0] += error * game_status_row1 * lr
   weights_5_neurons[1] += error * game_status_row2 * lr
   weights_5_neurons[2] += error * game_status_row3 * lr
   weights_5_neurons[3] += error * game_status_across1 * lr
   weights_5_neurons[4] += error * game_status_across2 * lr
   
   weights_5_neurons[5] += error * bias * lr
   print("Post Correction,",weights_5_neurons[0],",",weights_5_neurons[1],",",weights_5_neurons[2],",",weights_5_neurons[3],",",weights_5_neurons[4],",",weights_5_neurons[5],",",error)
   
# Teaching the Neural Network so that it build the weights_5_neurons  
for i in range(50) :
   Perceptron_5_neurons(1,0,0,0,0,1) 
   Perceptron_5_neurons(0,1,0,0,0,1) 
   Perceptron_5_neurons(0,0,1,0,0,1) 
   Perceptron_5_neurons(0,0,0,1,0,1) 
   Perceptron_5_neurons(0,0,0,0,1,1) 
   Perceptron_5_neurons(0,0,0,0,0,0) 


# Now see What it has learnt 

row1 = int(input())
row2 = int(input())
row3 = int(input())
across1 = int(input())
across2 = int(input())

FinalStatus = ActivationFunction_5_neurons(row1,weights_5_neurons[0],row2,weights_5_neurons[1],row3,weights_5_neurons[2],across1,weights_5_neurons[3],across2,weights_5_neurons[4],bias,weights_5_neurons[5])
print("Game Status", FinalStatus)   

