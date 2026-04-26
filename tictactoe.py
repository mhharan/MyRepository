# Check the versions of libraries
import numpy, random, os, time
from os import system
from time import sleep

lr = 1 #learning rate part of NeuralNetwork Perceptron Algorithm
bias = 1 #value of bias part of NeuralNetwork Perceptron Algorithm
weights_2_neurons = [random.random(),random.random(),random.random()] #weight for 2 Neuron NeuralNetwork as per Perceptron Algorithm
weights_8_neurons = [random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random()] #weight for 8 Neuron NeuralNetwork as per Perceptron Algorithm

##### Creating Neural Network Generic Functions ##### 
def ActivationFunction_2_nerons(input1, weights1, input2, weights2, bias, weights3) :
   outputP = input1*weights1+input2*weights2+bias*weights3

   if outputP > 0 : #activation function (here Heaviside) True or False comes from Neurons getting trained
      outputP = 1
   else :
      outputP = 0
	
   return outputP

def Perceptron_2_nerons(input1, input2, output) :
   outputP = ActivationFunction_2_nerons(input1,weights_2_neurons[0],input2,weights_2_neurons[1],bias,weights_2_neurons[2])
   
   error = output-outputP
   weights_2_neurons[0] += error * input1 * lr
   weights_2_neurons[1] += error * input2 * lr
   weights_2_neurons[2] += error * bias * lr
   
   
def ActivationFunction_8_neurons(input1, weights1, input2, weights2,input3, weights3, input4, weights4, input5, weights5, input6, weights6, input7, weights7,input8, weights8, bias, weights9) :
   outputP = input1*weights1+input2*weights2+input3*weights3+input4*weights4+input5*weights5+input6*weights6+input7*weights7+input8*weights8+bias*weights9

   if outputP > 0 : #activation function (here Heaviside) True or False comes from Neurons getting trained
      outputP = 1
   else :
      outputP = 0
	
   return outputP

def Perceptron_8_neurons(input1, input2, input3, input4, input5, input6, input7, input8,output) :
   outputP = ActivationFunction_8_neurons(input1,weights_8_neurons[0],input2,weights_8_neurons[1],input3,weights_8_neurons[2],input4,weights_8_neurons[3],input5,weights_8_neurons[4],input6,weights_8_neurons[5],input7,weights_8_neurons[6],input8,weights_8_neurons[7],bias,weights_8_neurons[8])   
   
   error = output-outputP
   weights_8_neurons[0] += error * input1 * lr
   weights_8_neurons[1] += error * input2 * lr
   weights_8_neurons[2] += error * input3 * lr
   weights_8_neurons[3] += error * input4 * lr
   weights_8_neurons[4] += error * input5 * lr
   weights_8_neurons[5] += error * input5 * lr
   weights_8_neurons[6] += error * input5 * lr
   weights_8_neurons[7] += error * input5 * lr
   
   weights_8_neurons[8] += error * bias * lr
   #print("PostCorrection,",weights_5_neurons[0],",",weights_5_neurons[1],",",weights_5_neurons[2],",",weights_5_neurons[3],",",weights_5_neurons[4],",",weights_5_neurons[5],",",error)
   
def Teach_2_neurons():   
	# Teaching the 2 Neuron Neural Network so that it learns to decide Row wise GameOver cominations   
	for i in range(100) :
	   Perceptron_2_nerons(1,1,0) # eg Cell 1 <> Cell 2 and Cell 2 <> Cell 3 -> StillToGo
	   Perceptron_2_nerons(1,0,0) # eg Cell 1 <> Cell 2 and Cell 2 = Cell 3 -> StillToGo
	   Perceptron_2_nerons(0,1,0) # eg Cell 1 = Cell 2 and Cell 2 <> Cell 3 -> StillToGo
	   Perceptron_2_nerons(0,0,1) # eg Cell 1 = Cell 2 and Cell 2 = Cell 3 -> GameOver
	   
def Teach_8_neurons():
	# Teaching the 8 Neuron Neural Network so that can judge GameOver  
	for i in range(100) :
	   Perceptron_8_neurons(1,0,0,0,0,0,0,0,1) #eg. Row 1 is GameOver, Row 2,3, Col 1,2,3, Across 1 and 2 not over  -> GameOver
	   Perceptron_8_neurons(0,1,0,0,0,0,0,0,1) #eg. Row 2 is GameOver, Row 1,3, Col 1,2,3, Across 1 and 2 not over  -> GameOver
	   Perceptron_8_neurons(0,0,1,0,0,0,0,0,1) #eg. Row 3 is GameOver, Row 1,2, Col 1,2,3, Across 1 and 2 not over  -> GameOver
	   Perceptron_8_neurons(0,0,0,1,0,0,0,0,1) #eg. Col 1 is GameOver, Row 1,2,3, Col 2,3, Across 1 and 2 not over  -> GameOver
	   Perceptron_8_neurons(0,0,0,0,1,0,0,0,1) #eg. Col 2 is GameOver, Row 1,2,3, Col 1,3, Across 1 and 2 not over  -> GameOver
	   Perceptron_8_neurons(1,0,0,0,0,1,0,0,1) #eg. Col 3 is GameOver, Row 1,2,3, Col 1,2, Across 1 and 2 not over  -> GameOver
	   Perceptron_8_neurons(0,0,0,0,0,0,1,0,1) #eg. Across 1 is GameOver, Row 1,2,3, Col 1,2,3 Across 2 not over  -> GameOver
	   Perceptron_8_neurons(0,0,0,0,0,0,0,1,1) #eg. Across 2 is GameOver, Row 1,2,3, Col 1,2,3 Across 1 not over  -> GameOver
	   Perceptron_8_neurons(0,0,0,0,0,0,0,0,0) #eg. Row 1,2,3, Col 1,2,3 Across 1,2 not over -> StillToGo

##### End of Generic Neural Functions ########## End of Generic Neural Functions #####

##### Main Body ########## Main Body #####
# Speciifc Functions for Tic Tac Toe
def AutoMode(board_row1,board_row2, board_row3):
	local_board_row1 = [0,0,0]
	local_board_row2 = [0,0,0]
	local_board_row3 = [0,0,0]
	local_board_row1[0] = board_row1[0]
	local_board_row1[1] = board_row1[1]
	local_board_row1[2] = board_row1[2]
	local_board_row2[0] = board_row2[0]
	local_board_row2[1] = board_row2[1]
	local_board_row2[2] = board_row2[2]
	local_board_row3[0] = board_row3[0]
	local_board_row3[1] = board_row3[1]
	local_board_row3[2] = board_row3[2]
	print("Computer is thinking...") 
	sleep(2)
	position = WinningMove(local_board_row1,local_board_row2, local_board_row3)
	#print("WinningPosition",position)
	if position == 0:
		position = BlockingMove(local_board_row1,local_board_row2, local_board_row3)
		#print("BlockingPosition",position)
		if position == 0:
			position = MakeSmartMove(local_board_row1,local_board_row2, local_board_row3)
			if position == 0:
				position = GetNextPosition(local_board_row1,local_board_row2, local_board_row3)

	return position	

def MakeSmartMove(board_row1,board_row2, board_row3):
	local_board_row1 = [0,0,0]
	local_board_row2 = [0,0,0]
	local_board_row3 = [0,0,0]
	local_board_row1[0] = board_row1[0]
	local_board_row1[1] = board_row1[1]
	local_board_row1[2] = board_row1[2]
	local_board_row2[0] = board_row2[0]
	local_board_row2[1] = board_row2[1]
	local_board_row2[2] = board_row2[2]
	local_board_row3[0] = board_row3[0]
	local_board_row3[1] = board_row3[1]
	local_board_row3[2] = board_row3[2]

	position = 21
	FinalStatus = 0
	while FinalStatus == 0 and position > 0:
		position = GetNextPosition(local_board_row1,local_board_row2, local_board_row3)
		if position == 10:
			local_board_row1[0] = 2
		if position == 11:
			local_board_row1[1] = 2
		if position == 12:
			local_board_row1[2] = 2
		if position == 20:
			local_board_row2[0] = 2
		if position == 21:
			local_board_row2[1] = 2
		if position == 22:
			local_board_row2[2] = 2
		if position == 30:
			local_board_row3[0] = 2
		if position == 31:
			local_board_row3[1] = 2
		if position == 32:
			local_board_row3[2] = 2
		
		nxt_position = WinningMove(local_board_row1,local_board_row2, local_board_row3)	
		if nxt_position == 10:
			local_board_row1[0] = 2
		if nxt_position == 11:
			local_board_row1[1] = 2
		if nxt_position == 12:
			local_board_row1[2] = 2
		if nxt_position == 20:
			local_board_row2[0] = 2
		if nxt_position == 21:
			local_board_row2[1] = 2
		if nxt_position == 22:
			local_board_row2[2] = 2
		if nxt_position == 30:
			local_board_row3[0] = 2
		if nxt_position == 31:
			local_board_row3[1] = 2
		if nxt_position == 32:
			local_board_row3[2] = 2

		FinalStatus = Check_Game_Status(local_board_row1,local_board_row2,local_board_row3)
		if FinalStatus == 0:
			if nxt_position == 10:
				local_board_row1[0] = 10
			if nxt_position == 11:
				local_board_row1[1] = 11
			if nxt_position == 12:
				local_board_row1[2] = 12
			if nxt_position == 20:
				local_board_row2[0] = 20
			if nxt_position == 21:
				local_board_row2[1] = 21
			if nxt_position == 22:
				local_board_row2[2] = 22
			if nxt_position == 30:
				local_board_row3[0] = 30
			if nxt_position == 31:
				local_board_row3[1] = 31
			if nxt_position == 32:
				local_board_row3[2] = 32

			if position == 10:
				local_board_row1[0] = -10
			if position == 11:
				local_board_row1[1] = -11
			if position == 12:
				local_board_row1[2] = -12
			if position == 20:
				local_board_row2[0] = -20
			if position == 21:
				local_board_row2[1] = -21
			if position == 22:
				local_board_row2[2] = -22
			if position == 30:
				local_board_row3[0] = -30
			if position == 31:
				local_board_row3[1] = -31
			if position == 32:
				local_board_row3[2] = -32
		
	
	return position	

def WinningMove(board_row1,board_row2, board_row3):
	local_board_row1 = [0,0,0]
	local_board_row2 = [0,0,0]
	local_board_row3 = [0,0,0]
	local_board_row1[0] = board_row1[0]
	local_board_row1[1] = board_row1[1]
	local_board_row1[2] = board_row1[2]
	local_board_row2[0] = board_row2[0]
	local_board_row2[1] = board_row2[1]
	local_board_row2[2] = board_row2[2]
	local_board_row3[0] = board_row3[0]
	local_board_row3[1] = board_row3[1]
	local_board_row3[2] = board_row3[2]

	position = 21
	FinalStatus = 0
	while FinalStatus == 0 and position > 0:
		position = GetNextPosition(local_board_row1,local_board_row2, local_board_row3)
		if position == 10:
			local_board_row1[0] = 2
		if position == 11:
			local_board_row1[1] = 2
		if position == 12:
			local_board_row1[2] = 2
		if position == 20:
			local_board_row2[0] = 2
		if position == 21:
			local_board_row2[1] = 2
		if position == 22:
			local_board_row2[2] = 2
		if position == 30:
			local_board_row3[0] = 2
		if position == 31:
			local_board_row3[1] = 2
		if position == 32:
			local_board_row3[2] = 2
			
		FinalStatus = Check_Game_Status(local_board_row1,local_board_row2,local_board_row3)
		if FinalStatus == 0:
			if position == 10:
				local_board_row1[0] = -10
			if position == 11:
				local_board_row1[1] = -11
			if position == 12:
				local_board_row1[2] = -12
			if position == 20:
				local_board_row2[0] = -20
			if position == 21:
				local_board_row2[1] = -21
			if position == 22:
				local_board_row2[2] = -22
			if position == 30:
				local_board_row3[0] = -30
			if position == 31:
				local_board_row3[1] = -31
			if position == 32:
				local_board_row3[2] = -32
		
	
	return position	


def BlockingMove(board_row1,board_row2, board_row3):
	local_board_row1 = [0,0,0]
	local_board_row2 = [0,0,0]
	local_board_row3 = [0,0,0]
	local_board_row1[0] = board_row1[0]
	local_board_row1[1] = board_row1[1]
	local_board_row1[2] = board_row1[2]
	local_board_row2[0] = board_row2[0]
	local_board_row2[1] = board_row2[1]
	local_board_row2[2] = board_row2[2]
	local_board_row3[0] = board_row3[0]
	local_board_row3[1] = board_row3[1]
	local_board_row3[2] = board_row3[2]

	position = 21
	FinalStatus = 0
	while FinalStatus == 0 and position > 0:
		position = GetNextPosition(local_board_row1,local_board_row2, local_board_row3)
		if position == 10:
			local_board_row1[0] = 1
		if position == 11:
			local_board_row1[1] = 1
		if position == 12:
			local_board_row1[2] = 1
		if position == 20:
			local_board_row2[0] = 1
		if position == 21:
			local_board_row2[1] = 1
		if position == 22:
			local_board_row2[2] = 1
		if position == 30:
			local_board_row3[0] = 1
		if position == 31:
			local_board_row3[1] = 1
		if position == 32:
			local_board_row3[2] = 1
			
		FinalStatus = Check_Game_Status(local_board_row1,local_board_row2,local_board_row3)
		if FinalStatus == 0:
			if position == 10:
				local_board_row1[0] = -10
			if position == 11:
				local_board_row1[1] = -11
			if position == 12:
				local_board_row1[2] = -12
			if position == 20:
				local_board_row2[0] = -20
			if position == 21:
				local_board_row2[1] = -21
			if position == 22:
				local_board_row2[2] = -22
			if position == 30:
				local_board_row3[0] = -30
			if position == 31:
				local_board_row3[1] = -31
			if position == 32:
				local_board_row3[2] = -32
		
	
	return position	

def GetNextPosition(board_row1,board_row2, board_row3):
	position = 20 # Start looking at middle row
	if GetEmptyCell(board_row2) > -1 :
		#print("AutoValue",position)
		return position + GetEmptyCell(board_row2)
	position = 10
	if GetEmptyCell(board_row1) > -1 :
		#print("AutoValue",position)
		return position + GetEmptyCell(board_row1)
	position = 30
	if GetEmptyCell(board_row3) > -1 :
		#print("AutoValue",position)
		return position + GetEmptyCell(board_row3)
	#print("No Empty Cell")	
	return 0	
	
		
def GetEmptyCell(board_row) :
	#print("Cell Value",board_row[0],board_row[1],board_row[2])
	if board_row[1]>2: # Start looking at middle cell first
		return 1
	if board_row[0]>2:
		return 0
	if board_row[2]>2:
		return 2
	return -1
		
def Check_Game_Status(board_row1,board_row2,board_row3):

	# Check the Board Values to Pass it to Neural Network with 2 Neurons the beauty is there is no IF conditions here
	check_game_row1=[0,0]
	check_game_row1[0]=abs(board_row1[0]-board_row1[1])
	check_game_row1[1]=abs(board_row1[1]-board_row1[2])
	check_game_row2=[0,0]
	check_game_row2[0]=abs(board_row2[0]-board_row2[1])
	check_game_row2[1]=abs(board_row2[1]-board_row2[2])
	check_game_row3=[0,0]
	check_game_row3[0]=abs(board_row3[0]-board_row3[1])
	check_game_row3[1]=abs(board_row3[1]-board_row3[2])
	
	check_game_down1=[0,0]
	check_game_down1[0]=abs(board_row1[0]-board_row2[0])
	check_game_down1[1]=abs(board_row2[0]-board_row3[0])
	check_game_down2=[0,0]
	check_game_down2[0]=abs(board_row1[1]-board_row2[1])
	check_game_down2[1]=abs(board_row2[1]-board_row3[1])
	check_game_down3=[0,0]
	check_game_down3[0]=abs(board_row1[2]-board_row2[2])
	check_game_down3[1]=abs(board_row2[2]-board_row3[2])

	check_game_across1=[0,0]
	check_game_across1[0]=abs(board_row1[0]-board_row2[1])
	check_game_across1[1]=abs(board_row2[1]-board_row3[2])
	check_game_across2=[0,0]
	check_game_across2[0]=abs(board_row3[0]-board_row2[1])
	check_game_across2[1]=abs(board_row2[1]-board_row1[2])
	 
	game_status_row1 = ActivationFunction_2_nerons(check_game_row1[0], weights_2_neurons[0], check_game_row1[1], weights_2_neurons[1], bias, weights_2_neurons[2])
	game_status_row2 = ActivationFunction_2_nerons(check_game_row2[0], weights_2_neurons[0], check_game_row2[1], weights_2_neurons[1], bias, weights_2_neurons[2])
	game_status_row3 = ActivationFunction_2_nerons(check_game_row3[0], weights_2_neurons[0], check_game_row3[1], weights_2_neurons[1], bias, weights_2_neurons[2])
	game_status_down1 = ActivationFunction_2_nerons(check_game_down1[0], weights_2_neurons[0], check_game_down1[1], weights_2_neurons[1], bias, weights_2_neurons[2])
	game_status_down2 = ActivationFunction_2_nerons(check_game_down2[0], weights_2_neurons[0], check_game_down2[1], weights_2_neurons[1], bias, weights_2_neurons[2])
	game_status_down3 = ActivationFunction_2_nerons(check_game_down3[0], weights_2_neurons[0], check_game_down3[1], weights_2_neurons[1], bias, weights_2_neurons[2])
	game_status_across1 = ActivationFunction_2_nerons(check_game_across1[0], weights_2_neurons[0], check_game_across1[1], weights_2_neurons[1], bias, weights_2_neurons[2])
	game_status_across2 = ActivationFunction_2_nerons(check_game_across2[0], weights_2_neurons[0], check_game_across2[1], weights_2_neurons[1], bias, weights_2_neurons[2])

	# Pass the output of 2 Neuron Neural Network as Input to 8 Neurons Neural Network for Overall Status
	FinalStatus = ActivationFunction_8_neurons(game_status_row1,weights_8_neurons[0],game_status_row2,weights_8_neurons[1],game_status_row3,weights_8_neurons[2],game_status_down1,weights_8_neurons[3],game_status_down2,weights_8_neurons[4],game_status_down3,weights_8_neurons[5],game_status_across1,weights_8_neurons[6],game_status_across2,weights_8_neurons[7],bias,weights_8_neurons[8])
	return FinalStatus

################################
################################
# Game Related code Startes Here
################################
################################	   
Teach_2_neurons()
Teach_8_neurons()
   
# Tic Tac Board Status 
board_row1 = [10,11,12]
board_row2 = [20,21,22]
board_row3 = [30,31,32]
FinalStatus=0
PlayerNumber=2
automode = 1
position = 21
while FinalStatus == 0 and position > 0:
	if PlayerNumber == 1:
		PlayerNumber = 2
	else:
		PlayerNumber = 1

	_ = system('cls')
	print("")
	print("Tic Tac Toe Board:Player Number", PlayerNumber)
	print("[ %2d ] [ %2d ] [ %2d ]" %(board_row1[0],board_row1[1],board_row1[2]))   
	print("[ %2d ] [ %2d ] [ %2d ]" %(board_row2[0],board_row2[1],board_row2[2]))   
	print("[ %2d ] [ %2d ] [ %2d ]" %(board_row3[0],board_row3[1],board_row3[2]))
	print("")
	print("Input the Cell Number say 10,20, 21 etc or 0 to EXIT")

	if PlayerNumber == 1:
		position=int(input())
	else:
		if automode == 0:
			position=int(input())
		else:
			position=AutoMode(board_row1, board_row2, board_row3)
			#print("AutoMove Position:",position)
			
	if position == 10:
		board_row1[0]=PlayerNumber
	if position == 11:
		board_row1[1]=PlayerNumber
	if position == 12:
		board_row1[2]=PlayerNumber
	if position == 20:
		board_row2[0]=PlayerNumber
	if position == 21:
		board_row2[1]=PlayerNumber
	if position == 22:
		board_row2[2]=PlayerNumber
	if position == 30:
		board_row3[0]=PlayerNumber
	if position == 31:
		board_row3[1]=PlayerNumber
	if position == 32:
		board_row3[2]=PlayerNumber

	FinalStatus = Check_Game_Status(board_row1,board_row2,board_row3)
	#print("Game Status",FinalStatus)
	sleep(2)
	
if FinalStatus == 1: 	
	print("Game Won By Player:-", PlayerNumber)   
	print("[ %2d ] [ %2d ] [ %2d ]" %(board_row1[0],board_row1[1],board_row1[2]))   
	print("[ %2d ] [ %2d ] [ %2d ]" %(board_row2[0],board_row2[1],board_row2[2]))   
	print("[ %2d ] [ %2d ] [ %2d ]" %(board_row3[0],board_row3[1],board_row3[2]))
#	print("")

else:
	print("Game Draw !!!")   
