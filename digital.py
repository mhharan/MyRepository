# Check the versions of libraries
import random, os, time
import numpy as np
import pickle

from os import system
from time import sleep

import network

training_data=[None]*15

to_learn =0;
print("To Load the Lesson already Learnt Type 0, ELSE To Teach Counting Type 1")
to_learn=int(input())
if to_learn:
	# Take Input 
	board_row1 = [' ',' ',' ']
	board_row2 = [' ',' ',' ']
	board_row3 = [' ',' ',' ']
	board_row4 = [' ',' ',' ']
	board_row5 = [' ',' ',' ']
	InputNumber=0
	position = 21
	while position != 100:
		_ = system('cls')
		print("")
		print("LEARNING MODE: Give Digital Representation of Number One")
		print(" "," ","0", "1", "2")   
		print(" ","+","-", "-", "-", "+")   
		print("1","|", board_row1[0], board_row1[1],  board_row1[2], "|")   
		print("2","|", board_row2[0], board_row2[1],  board_row2[2], "|")   
		print("3","|", board_row3[0], board_row3[1],  board_row3[2], "|")   
		print("4","|", board_row4[0], board_row4[1],  board_row4[2], "|")   
		print("5","|", board_row5[0], board_row5[1],  board_row5[2], "|")   
		print(" ","+","-", "-", "-", "+")   
		print("")
		print("Input the Cell Number say 10,20, 21 etc or 0 to CLEAR, 100 to EXIT")

		position=int(input())
		if position == 10:
			board_row1[0]='X'
		if position == 11:
			board_row1[1]='X'
		if position == 12:
			board_row1[2]='X'
		if position == 20:
			board_row2[0]='X'
		if position == 21:
			board_row2[1]='X'
		if position == 22:
			board_row2[2]='X'
		if position == 30:
			board_row3[0]='X'
		if position == 31:
			board_row3[1]='X'
		if position == 32:
			board_row3[2]='X'
		if position == 40:
			board_row4[0]='X'
		if position == 41:
			board_row4[1]='X'
		if position == 42:
			board_row4[2]='X'
		if position == 50:
			board_row5[0]='X'
		if position == 51:
			board_row5[1]='X'
		if position == 52:
			board_row5[2]='X'

		if position == 0:
			board_row1 = [' ',' ',' ']
			board_row2 = [' ',' ',' ']
			board_row3 = [' ',' ',' ']
			board_row4 = [' ',' ',' ']
			board_row5 = [' ',' ',' ']
			



	a = np.array(([board_row1[0]=='X'],[board_row1[1]=='X'],[board_row1[2]=='X'],[board_row2[0]=='X'],[board_row2[1]=='X'],[board_row2[2]=='X'],[board_row3[0]=='X'],[board_row3[1]=='X'],[board_row3[2]=='X'],[board_row4[0]=='X'],[board_row4[1]=='X'],[board_row4[2]=='X'],[board_row5[0]=='X'],[board_row5[1]=='X'],[board_row5[2]=='X']),dtype=np.float32)
	b = np.array(([1],[0],[0],[0],[0]))
	training_data[0]=tuple((a,b))
	training_data[5]=tuple((a,b))
	training_data[10]=tuple((a,b))

	# Take Input 
	board_row1 = [' ',' ',' ']
	board_row2 = [' ',' ',' ']
	board_row3 = [' ',' ',' ']
	board_row4 = [' ',' ',' ']
	board_row5 = [' ',' ',' ']
	InputNumber=0
	position = 21
	while position != 100:
		_ = system('cls')
		print("")
		print("LEARNING MODE: Give Digital Representation of Number Two")
		print(" "," ","0", "1", "2")   
		print(" ","+","-", "-", "-", "+")   
		print("1","|", board_row1[0], board_row1[1],  board_row1[2], "|")   
		print("2","|", board_row2[0], board_row2[1],  board_row2[2], "|")   
		print("3","|", board_row3[0], board_row3[1],  board_row3[2], "|")   
		print("4","|", board_row4[0], board_row4[1],  board_row4[2], "|")   
		print("5","|", board_row5[0], board_row5[1],  board_row5[2], "|")   
		print(" ","+","-", "-", "-", "+")   
		print("")
		print("Input the Cell Number say 10,20, 21 etc or 0 to CLEAR, 100 to EXIT")

		position=int(input())
		if position == 10:
			board_row1[0]='X'
		if position == 11:
			board_row1[1]='X'
		if position == 12:
			board_row1[2]='X'
		if position == 20:
			board_row2[0]='X'
		if position == 21:
			board_row2[1]='X'
		if position == 22:
			board_row2[2]='X'
		if position == 30:
			board_row3[0]='X'
		if position == 31:
			board_row3[1]='X'
		if position == 32:
			board_row3[2]='X'
		if position == 40:
			board_row4[0]='X'
		if position == 41:
			board_row4[1]='X'
		if position == 42:
			board_row4[2]='X'
		if position == 50:
			board_row5[0]='X'
		if position == 51:
			board_row5[1]='X'
		if position == 52:
			board_row5[2]='X'

		if position == 0:
			board_row1 = [' ',' ',' ']
			board_row2 = [' ',' ',' ']
			board_row3 = [' ',' ',' ']
			board_row4 = [' ',' ',' ']
			board_row5 = [' ',' ',' ']
			



	a = np.array(([board_row1[0]=='X'],[board_row1[1]=='X'],[board_row1[2]=='X'],[board_row2[0]=='X'],[board_row2[1]=='X'],[board_row2[2]=='X'],[board_row3[0]=='X'],[board_row3[1]=='X'],[board_row3[2]=='X'],[board_row4[0]=='X'],[board_row4[1]=='X'],[board_row4[2]=='X'],[board_row5[0]=='X'],[board_row5[1]=='X'],[board_row5[2]=='X']),dtype=np.float32)
	b = np.array(([0],[1],[0],[0],[0]))
	training_data[1]=tuple((a,b))
	training_data[6]=tuple((a,b))
	training_data[11]=tuple((a,b))


	# Take Input 
	board_row1 = [' ',' ',' ']
	board_row2 = [' ',' ',' ']
	board_row3 = [' ',' ',' ']
	board_row4 = [' ',' ',' ']
	board_row5 = [' ',' ',' ']
	InputNumber=0
	position = 21
	while position != 100:
		_ = system('cls')
		print("")
		print("LEARNING MODE: Give Digital Representation of Number Three")
		print(" "," ","0", "1", "2")   
		print(" ","+","-", "-", "-", "+")   
		print("1","|", board_row1[0], board_row1[1],  board_row1[2], "|")   
		print("2","|", board_row2[0], board_row2[1],  board_row2[2], "|")   
		print("3","|", board_row3[0], board_row3[1],  board_row3[2], "|")   
		print("4","|", board_row4[0], board_row4[1],  board_row4[2], "|")   
		print("5","|", board_row5[0], board_row5[1],  board_row5[2], "|")   
		print(" ","+","-", "-", "-", "+")   
		print("")
		print("Input the Cell Number say 10,20, 21 etc or 0 to CLEAR, 100 to EXIT")

		position=int(input())
		if position == 10:
			board_row1[0]='X'
		if position == 11:
			board_row1[1]='X'
		if position == 12:
			board_row1[2]='X'
		if position == 20:
			board_row2[0]='X'
		if position == 21:
			board_row2[1]='X'
		if position == 22:
			board_row2[2]='X'
		if position == 30:
			board_row3[0]='X'
		if position == 31:
			board_row3[1]='X'
		if position == 32:
			board_row3[2]='X'
		if position == 40:
			board_row4[0]='X'
		if position == 41:
			board_row4[1]='X'
		if position == 42:
			board_row4[2]='X'
		if position == 50:
			board_row5[0]='X'
		if position == 51:
			board_row5[1]='X'
		if position == 52:
			board_row5[2]='X'

		if position == 0:
			board_row1 = [' ',' ',' ']
			board_row2 = [' ',' ',' ']
			board_row3 = [' ',' ',' ']
			board_row4 = [' ',' ',' ']
			board_row5 = [' ',' ',' ']
			



	a = np.array(([board_row1[0]=='X'],[board_row1[1]=='X'],[board_row1[2]=='X'],[board_row2[0]=='X'],[board_row2[1]=='X'],[board_row2[2]=='X'],[board_row3[0]=='X'],[board_row3[1]=='X'],[board_row3[2]=='X'],[board_row4[0]=='X'],[board_row4[1]=='X'],[board_row4[2]=='X'],[board_row5[0]=='X'],[board_row5[1]=='X'],[board_row5[2]=='X']),dtype=np.float32)
	b = np.array(([0],[0],[1],[0],[0]))
	training_data[2]=tuple((a,b))
	training_data[7]=tuple((a,b))
	training_data[12]=tuple((a,b))

	# Take Input 
	board_row1 = [' ',' ',' ']
	board_row2 = [' ',' ',' ']
	board_row3 = [' ',' ',' ']
	board_row4 = [' ',' ',' ']
	board_row5 = [' ',' ',' ']
	InputNumber=0
	position = 21
	while position != 100:
		_ = system('cls')
		print("")
		print("LEARNING MODE: Give Digital Representation of Number Four")
		print(" "," ","0", "1", "2")   
		print(" ","+","-", "-", "-", "+")   
		print("1","|", board_row1[0], board_row1[1],  board_row1[2], "|")   
		print("2","|", board_row2[0], board_row2[1],  board_row2[2], "|")   
		print("3","|", board_row3[0], board_row3[1],  board_row3[2], "|")   
		print("4","|", board_row4[0], board_row4[1],  board_row4[2], "|")   
		print("5","|", board_row5[0], board_row5[1],  board_row5[2], "|")   
		print(" ","+","-", "-", "-", "+")   
		print("")
		print("Input the Cell Number say 10,20, 21 etc or 0 to CLEAR, 100 to EXIT")

		position=int(input())
		if position == 10:
			board_row1[0]='X'
		if position == 11:
			board_row1[1]='X'
		if position == 12:
			board_row1[2]='X'
		if position == 20:
			board_row2[0]='X'
		if position == 21:
			board_row2[1]='X'
		if position == 22:
			board_row2[2]='X'
		if position == 30:
			board_row3[0]='X'
		if position == 31:
			board_row3[1]='X'
		if position == 32:
			board_row3[2]='X'
		if position == 40:
			board_row4[0]='X'
		if position == 41:
			board_row4[1]='X'
		if position == 42:
			board_row4[2]='X'
		if position == 50:
			board_row5[0]='X'
		if position == 51:
			board_row5[1]='X'
		if position == 52:
			board_row5[2]='X'

		if position == 0:
			board_row1 = [' ',' ',' ']
			board_row2 = [' ',' ',' ']
			board_row3 = [' ',' ',' ']
			board_row4 = [' ',' ',' ']
			board_row5 = [' ',' ',' ']
			



	a = np.array(([board_row1[0]=='X'],[board_row1[1]=='X'],[board_row1[2]=='X'],[board_row2[0]=='X'],[board_row2[1]=='X'],[board_row2[2]=='X'],[board_row3[0]=='X'],[board_row3[1]=='X'],[board_row3[2]=='X'],[board_row4[0]=='X'],[board_row4[1]=='X'],[board_row4[2]=='X'],[board_row5[0]=='X'],[board_row5[1]=='X'],[board_row5[2]=='X']),dtype=np.float32)
	b = np.array(([0],[0],[0],[1],[0]))
	training_data[3]=tuple((a,b))
	training_data[8]=tuple((a,b))
	training_data[13]=tuple((a,b))

	# Take Input 
	board_row1 = [' ',' ',' ']
	board_row2 = [' ',' ',' ']
	board_row3 = [' ',' ',' ']
	board_row4 = [' ',' ',' ']
	board_row5 = [' ',' ',' ']
	InputNumber=0
	position = 21
	while position != 100:
		_ = system('cls')
		print("")
		print("LEARNING MODE: Give Digital Representation of Number Five")
		print(" "," ","0", "1", "2")   
		print(" ","+","-", "-", "-", "+")   
		print("1","|", board_row1[0], board_row1[1],  board_row1[2], "|")   
		print("2","|", board_row2[0], board_row2[1],  board_row2[2], "|")   
		print("3","|", board_row3[0], board_row3[1],  board_row3[2], "|")   
		print("4","|", board_row4[0], board_row4[1],  board_row4[2], "|")   
		print("5","|", board_row5[0], board_row5[1],  board_row5[2], "|")   
		print(" ","+","-", "-", "-", "+")   
		print("")
		print("Input the Cell Number say 10,20, 21 etc or 0 to CLEAR, 100 to EXIT")

		position=int(input())
		if position == 10:
			board_row1[0]='X'
		if position == 11:
			board_row1[1]='X'
		if position == 12:
			board_row1[2]='X'
		if position == 20:
			board_row2[0]='X'
		if position == 21:
			board_row2[1]='X'
		if position == 22:
			board_row2[2]='X'
		if position == 30:
			board_row3[0]='X'
		if position == 31:
			board_row3[1]='X'
		if position == 32:
			board_row3[2]='X'
		if position == 40:
			board_row4[0]='X'
		if position == 41:
			board_row4[1]='X'
		if position == 42:
			board_row4[2]='X'
		if position == 50:
			board_row5[0]='X'
		if position == 51:
			board_row5[1]='X'
		if position == 52:
			board_row5[2]='X'

		if position == 0:
			board_row1 = [' ',' ',' ']
			board_row2 = [' ',' ',' ']
			board_row3 = [' ',' ',' ']
			board_row4 = [' ',' ',' ']
			board_row5 = [' ',' ',' ']
			



	a = np.array(([board_row1[0]=='X'],[board_row1[1]=='X'],[board_row1[2]=='X'],[board_row2[0]=='X'],[board_row2[1]=='X'],[board_row2[2]=='X'],[board_row3[0]=='X'],[board_row3[1]=='X'],[board_row3[2]=='X'],[board_row4[0]=='X'],[board_row4[1]=='X'],[board_row4[2]=='X'],[board_row5[0]=='X'],[board_row5[1]=='X'],[board_row5[2]=='X']),dtype=np.float32)
	b = np.array(([0],[0],[0],[0],[1]))
	training_data[4]=tuple((a,b))
	training_data[9]=tuple((a,b))
	training_data[14]=tuple((a,b))

	file = open('digits.data', 'wb')
	pickle.dump(training_data, file)
	file.close()

file = open('digits.data', 'rb')
lesson_data = pickle.load(file)
#print(lesson_data)
#keeptrying=int(input())
# close the file
file.close()
keeptrying=0

while keeptrying==0:
	# Try Giving  Input 
	board_row1 = [' ',' ',' ']
	board_row2 = [' ',' ',' ']
	board_row3 = [' ',' ',' ']
	board_row4 = [' ',' ',' ']
	board_row5 = [' ',' ',' ']
	InputNumber=0
	position = 21
	while position != 100:
		_ = system('cls')
		print("")
		print("TESTING MODE: Give Digital Representation of Number ")
		print(" "," ","0", "1", "2")   
		print(" ","+","-", "-", "-", "+")   
		print("1","|", board_row1[0], board_row1[1],  board_row1[2], "|")   
		print("2","|", board_row2[0], board_row2[1],  board_row2[2], "|")   
		print("3","|", board_row3[0], board_row3[1],  board_row3[2], "|")   
		print("4","|", board_row4[0], board_row4[1],  board_row4[2], "|")   
		print("5","|", board_row5[0], board_row5[1],  board_row5[2], "|")   
		print(" ","+","-", "-", "-", "+")   
		print("")
		print("Input the Cell Number say 10,20, 21 etc or 0 to CLEAR, 100 to EXIT")

		position=int(input())
		if position == 10:
			board_row1[0]='X'
		if position == 11:
			board_row1[1]='X'
		if position == 12:
			board_row1[2]='X'
		if position == 20:
			board_row2[0]='X'
		if position == 21:
			board_row2[1]='X'
		if position == 22:
			board_row2[2]='X'
		if position == 30:
			board_row3[0]='X'
		if position == 31:
			board_row3[1]='X'
		if position == 32:
			board_row3[2]='X'
		if position == 40:
			board_row4[0]='X'
		if position == 41:
			board_row4[1]='X'
		if position == 42:
			board_row4[2]='X'
		if position == 50:
			board_row5[0]='X'
		if position == 51:
			board_row5[1]='X'
		if position == 52:
			board_row5[2]='X'

		if position == 0:
			board_row1 = [' ',' ',' ']
			board_row2 = [' ',' ',' ']
			board_row3 = [' ',' ',' ']
			board_row4 = [' ',' ',' ']
			board_row5 = [' ',' ',' ']
			



	test_data = np.array(([board_row1[0]=='X'],[board_row1[1]=='X'],[board_row1[2]=='X'],[board_row2[0]=='X'],[board_row2[1]=='X'],[board_row2[2]=='X'],[board_row3[0]=='X'],[board_row3[1]=='X'],[board_row3[2]=='X'],[board_row4[0]=='X'],[board_row4[1]=='X'],[board_row4[2]=='X'],[board_row5[0]=='X'],[board_row5[1]=='X'],[board_row5[2]=='X']),dtype=np.float32)

	net = network.Network([15, 10, 5])
	net.SGD(lesson_data, 100, 5, 1)
	output = np.argmax(net.feedforward(test_data))+1
	print("You Typed Number:",output)
	print("To try again type 0, else type 1")
	keeptrying=int(input())