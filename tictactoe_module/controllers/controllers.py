# -*- coding: utf-8 -*-
from odoo import http
# Check the versions of libraries
import numpy, random, os, time
from os import system
from time import sleep


class TICTACTOEWebsite(http.Controller):
    # global lr #learning rate part of NeuralNetwork Perceptron Algorithm
    # global bias #value of bias part of NeuralNetwork Perceptron Algorithm
    # global weights_2_neurons #weight for 2 Neuron NeuralNetwork as per Perceptron Algorithm
    # global weights_8_neurons #weight for 8 Neuron NeuralNetwork as per Perceptron Algorithm

    # global board_row1
    # global board_row2
    # global board_row3
    # global FinalStatus
    # global PlayerNumber
    # global board_message
    # global automode
    # global position

    lr = 1 #learning rate part of NeuralNetwork Perceptron Algorithm
    bias = 1 #value of bias part of NeuralNetwork Perceptron Algorithm
    weights_2_neurons = [random.random(),random.random(),random.random()] #weight for 2 Neuron NeuralNetwork as per Perceptron Algorithm
    weights_8_neurons = [random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random()] #weight for 8 Neuron NeuralNetwork as per Perceptron Algorithm

    board_row1 = [10,11,12]
    board_row2 = [20,21,22]
    board_row3 = [30,31,32]
    FinalStatus = 0
    PlayerNumber = 0
    board_message = "Ready !!!"
    automode = 1
    position = 0

    def ResetGame(self) :
        TICTACTOEWebsite.board_row1 = [10,11,12]
        TICTACTOEWebsite.board_row2 = [20,21,22]
        TICTACTOEWebsite.board_row3 = [30,31,32]
        TICTACTOEWebsite.FinalStatus = 0
        TICTACTOEWebsite.PlayerNumber = 0
        TICTACTOEWebsite.board_message = "Ready !!!"
        TICTACTOEWebsite.automode = 1
        TICTACTOEWebsite.position = 0

    def LearnGame(self) :
        self.Teach_2_neurons()
        self.Teach_8_neurons()


    def ActivationFunction_2_nerons(self, input1, weights1, input2, weights2, bias, weights3) :
       outputP = input1*weights1+input2*weights2+bias*weights3

       if outputP > 0 : #activation function (here Heaviside) True or False comes from Neurons getting trained
          outputP = 1
       else :
          outputP = 0
        
       return outputP

    def Perceptron_2_nerons(self, input1, input2, output) :
       outputP = self.ActivationFunction_2_nerons(input1,TICTACTOEWebsite.weights_2_neurons[0],input2,TICTACTOEWebsite.weights_2_neurons[1],TICTACTOEWebsite.bias,TICTACTOEWebsite.weights_2_neurons[2])
       
       error = output-outputP
       TICTACTOEWebsite.weights_2_neurons[0] += error * input1 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_2_neurons[1] += error * input2 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_2_neurons[2] += error * TICTACTOEWebsite.bias * TICTACTOEWebsite.lr
       
       
    def ActivationFunction_8_neurons(self, input1, weights1, input2, weights2,input3, weights3, input4, weights4, input5, weights5, input6, weights6, input7, weights7,input8, weights8, bias, weights9) :
       outputP = input1*weights1+input2*weights2+input3*weights3+input4*weights4+input5*weights5+input6*weights6+input7*weights7+input8*weights8+bias*weights9

       if outputP > 0 : #activation function (here Heaviside) True or False comes from Neurons getting trained
          outputP = 1
       else :
          outputP = 0
        
       return outputP

    def Perceptron_8_neurons(self, input1, input2, input3, input4, input5, input6, input7, input8,output) :
       outputP = self.ActivationFunction_8_neurons(input1,TICTACTOEWebsite.weights_8_neurons[0],input2,TICTACTOEWebsite.weights_8_neurons[1],input3,TICTACTOEWebsite.weights_8_neurons[2],input4,TICTACTOEWebsite.weights_8_neurons[3],input5,TICTACTOEWebsite.weights_8_neurons[4],input6,TICTACTOEWebsite.weights_8_neurons[5],input7,TICTACTOEWebsite.weights_8_neurons[6],input8,TICTACTOEWebsite.weights_8_neurons[7],TICTACTOEWebsite.bias,TICTACTOEWebsite.weights_8_neurons[8])   
       
       error = output-outputP
       TICTACTOEWebsite.weights_8_neurons[0] += error * input1 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_8_neurons[1] += error * input2 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_8_neurons[2] += error * input3 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_8_neurons[3] += error * input4 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_8_neurons[4] += error * input5 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_8_neurons[5] += error * input5 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_8_neurons[6] += error * input5 * TICTACTOEWebsite.lr
       TICTACTOEWebsite.weights_8_neurons[7] += error * input5 * TICTACTOEWebsite.lr
       
       TICTACTOEWebsite.weights_8_neurons[8] += error * TICTACTOEWebsite.bias * TICTACTOEWebsite.lr
       #print("PostCorrection,",weights_5_neurons[0],",",weights_5_neurons[1],",",weights_5_neurons[2],",",weights_5_neurons[3],",",weights_5_neurons[4],",",weights_5_neurons[5],",",error)
       
    def Teach_2_neurons(self):   
        # Teaching the 2 Neuron Neural Network so that it learns to decide Row wise GameOver cominations   
        for i in range(100) :
           self.Perceptron_2_nerons(1,1,0)
           self.Perceptron_2_nerons(1,0,0)
           self.Perceptron_2_nerons(0,1,0)
           self.Perceptron_2_nerons(0,0,1)
           
    def Teach_8_neurons(self):
        # Teaching the 8 Neuron Neural Network so that can judge GameOver  
        for i in range(100) :
           self.Perceptron_8_neurons(1,0,0,0,0,0,0,0,1) 
           self.Perceptron_8_neurons(0,1,0,0,0,0,0,0,1) 
           self.Perceptron_8_neurons(0,0,1,0,0,0,0,0,1) 
           self.Perceptron_8_neurons(0,0,0,1,0,0,0,0,1) 
           self.Perceptron_8_neurons(0,0,0,0,1,0,0,0,1) 
           self.Perceptron_8_neurons(1,0,0,0,0,1,0,0,1) 
           self.Perceptron_8_neurons(0,0,0,0,0,0,1,0,1) 
           self.Perceptron_8_neurons(0,0,0,0,0,0,0,1,1) 
           self.Perceptron_8_neurons(0,0,0,0,0,0,0,0,0) 

    ##### End of Generic Neural Functions ########## End of Generic Neural Functions #####

    ##### Main Body ########## Main Body #####
    # Speciifc Functions for Tic Tac Toe
    def AutoMode(self, board_row1,board_row2, board_row3):
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
        TICTACTOEWebsite.board_message="Computer is thinking..." 
        sleep(2)
        TICTACTOEWebsite.position = self.WinningMove(local_board_row1,local_board_row2, local_board_row3)
        #print("WinningPosition",position)
        if TICTACTOEWebsite.position == 0:
            TICTACTOEWebsite.position = self.BlockingMove(local_board_row1,local_board_row2, local_board_row3)
            #print("BlockingPosition",position)
            if TICTACTOEWebsite.position == 0:
                TICTACTOEWebsite.position = self.MakeSmartMove(local_board_row1,local_board_row2, local_board_row3)
                if TICTACTOEWebsite.position == 0:
                    TICTACTOEWebsite.position = self.GetNextPosition(local_board_row1,local_board_row2, local_board_row3)

        return TICTACTOEWebsite.position	

    def MakeSmartMove(self, board_row1,board_row2, board_row3):
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

        TICTACTOEWebsite.position = 21
        TICTACTOEWebsite.FinalStatus = 0
        while TICTACTOEWebsite.FinalStatus == 0 and TICTACTOEWebsite.position > 0:
            TICTACTOEWebsite.position = self.GetNextPosition(local_board_row1,local_board_row2, local_board_row3)
            if TICTACTOEWebsite.position == 10:
                local_board_row1[0] = 2
            if TICTACTOEWebsite.position == 11:
                local_board_row1[1] = 2
            if TICTACTOEWebsite.position == 12:
                local_board_row1[2] = 2
            if TICTACTOEWebsite.position == 20:
                local_board_row2[0] = 2
            if TICTACTOEWebsite.position == 21:
                local_board_row2[1] = 2
            if TICTACTOEWebsite.position == 22:
                local_board_row2[2] = 2
            if TICTACTOEWebsite.position == 30:
                local_board_row3[0] = 2
            if TICTACTOEWebsite.position == 31:
                local_board_row3[1] = 2
            if TICTACTOEWebsite.position == 32:
                local_board_row3[2] = 2
            
            nxt_position = self.WinningMove(local_board_row1,local_board_row2, local_board_row3)	
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

            TICTACTOEWebsite.FinalStatus = self.Check_Game_Status(local_board_row1,local_board_row2,local_board_row3)
            if TICTACTOEWebsite.FinalStatus == 0:
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

                if TICTACTOEWebsite.position == 10:
                    local_board_row1[0] = -10
                if TICTACTOEWebsite.position == 11:
                    local_board_row1[1] = -11
                if TICTACTOEWebsite.position == 12:
                    local_board_row1[2] = -12
                if TICTACTOEWebsite.position == 20:
                    local_board_row2[0] = -20
                if TICTACTOEWebsite.position == 21:
                    local_board_row2[1] = -21
                if TICTACTOEWebsite.position == 22:
                    local_board_row2[2] = -22
                if TICTACTOEWebsite.position == 30:
                    local_board_row3[0] = -30
                if TICTACTOEWebsite.position == 31:
                    local_board_row3[1] = -31
                if TICTACTOEWebsite.position == 32:
                    local_board_row3[2] = -32
            
        
        return TICTACTOEWebsite.position	

    def WinningMove(self, board_row1,board_row2, board_row3):
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

        TICTACTOEWebsite.position = 21
        TICTACTOEWebsite.FinalStatus = 0
        while TICTACTOEWebsite.FinalStatus == 0 and TICTACTOEWebsite.position > 0:
            TICTACTOEWebsite.position = self.GetNextPosition(local_board_row1,local_board_row2, local_board_row3)
            if TICTACTOEWebsite.position == 10:
                local_board_row1[0] = 2
            if TICTACTOEWebsite.position == 11:
                local_board_row1[1] = 2
            if TICTACTOEWebsite.position == 12:
                local_board_row1[2] = 2
            if TICTACTOEWebsite.position == 20:
                local_board_row2[0] = 2
            if TICTACTOEWebsite.position == 21:
                local_board_row2[1] = 2
            if TICTACTOEWebsite.position == 22:
                local_board_row2[2] = 2
            if TICTACTOEWebsite.position == 30:
                local_board_row3[0] = 2
            if TICTACTOEWebsite.position == 31:
                local_board_row3[1] = 2
            if TICTACTOEWebsite.position == 32:
                local_board_row3[2] = 2
                
            TICTACTOEWebsite.FinalStatus = self.Check_Game_Status(local_board_row1,local_board_row2,local_board_row3)
            if TICTACTOEWebsite.FinalStatus == 0:
                if TICTACTOEWebsite.position == 10:
                    local_board_row1[0] = -10
                if TICTACTOEWebsite.position == 11:
                    local_board_row1[1] = -11
                if TICTACTOEWebsite.position == 12:
                    local_board_row1[2] = -12
                if TICTACTOEWebsite.position == 20:
                    local_board_row2[0] = -20
                if TICTACTOEWebsite.position == 21:
                    local_board_row2[1] = -21
                if TICTACTOEWebsite.position == 22:
                    local_board_row2[2] = -22
                if TICTACTOEWebsite.position == 30:
                    local_board_row3[0] = -30
                if TICTACTOEWebsite.position == 31:
                    local_board_row3[1] = -31
                if TICTACTOEWebsite.position == 32:
                    local_board_row3[2] = -32
            
        
        return TICTACTOEWebsite.position	


    def BlockingMove(self, board_row1,board_row2, board_row3):
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
            position = self.GetNextPosition(local_board_row1,local_board_row2, local_board_row3)
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
                
            FinalStatus = self.Check_Game_Status(local_board_row1,local_board_row2,local_board_row3)
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

    def GetNextPosition(self, board_row1,board_row2, board_row3):
        position = 20 # Start looking at middle row
        if self.GetEmptyCell(board_row2) > -1 :
            #print("AutoValue",position)
            return position + self.GetEmptyCell(board_row2)
        position = 10
        if self.GetEmptyCell(board_row1) > -1 :
            #print("AutoValue",position)
            return position + self.GetEmptyCell(board_row1)
        position = 30
        if self.GetEmptyCell(board_row3) > -1 :
            #print("AutoValue",position)
            return position + self.GetEmptyCell(board_row3)
        #print("No Empty Cell")	
        return 0	
        
            
    def GetEmptyCell(self, board_row) :
        #print("Cell Value",board_row[0],board_row[1],board_row[2])
        if board_row[1]>2: # Start looking at middle cell first
            return 1
        if board_row[0]>2:
            return 0
        if board_row[2]>2:
            return 2
        return -1
            
    def Check_Game_Status(self, board_row1,board_row2,board_row3):

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
         
        game_status_row1 = self.ActivationFunction_2_nerons(check_game_row1[0], TICTACTOEWebsite.weights_2_neurons[0], check_game_row1[1], TICTACTOEWebsite.weights_2_neurons[1], TICTACTOEWebsite.bias, TICTACTOEWebsite.weights_2_neurons[2])
        game_status_row2 = self.ActivationFunction_2_nerons(check_game_row2[0], TICTACTOEWebsite.weights_2_neurons[0], check_game_row2[1], TICTACTOEWebsite.weights_2_neurons[1], TICTACTOEWebsite.bias, TICTACTOEWebsite.weights_2_neurons[2])
        game_status_row3 = self.ActivationFunction_2_nerons(check_game_row3[0], TICTACTOEWebsite.weights_2_neurons[0], check_game_row3[1], TICTACTOEWebsite.weights_2_neurons[1], TICTACTOEWebsite.bias, TICTACTOEWebsite.weights_2_neurons[2])
        game_status_down1 = self.ActivationFunction_2_nerons(check_game_down1[0], TICTACTOEWebsite.weights_2_neurons[0], check_game_down1[1], TICTACTOEWebsite.weights_2_neurons[1], TICTACTOEWebsite.bias, TICTACTOEWebsite.weights_2_neurons[2])
        game_status_down2 = self.ActivationFunction_2_nerons(check_game_down2[0], TICTACTOEWebsite.weights_2_neurons[0], check_game_down2[1], TICTACTOEWebsite.weights_2_neurons[1], TICTACTOEWebsite.bias, TICTACTOEWebsite.weights_2_neurons[2])
        game_status_down3 = self.ActivationFunction_2_nerons(check_game_down3[0], TICTACTOEWebsite.weights_2_neurons[0], check_game_down3[1], TICTACTOEWebsite.weights_2_neurons[1], TICTACTOEWebsite.bias, TICTACTOEWebsite.weights_2_neurons[2])
        game_status_across1 = self.ActivationFunction_2_nerons(check_game_across1[0], TICTACTOEWebsite.weights_2_neurons[0], check_game_across1[1], TICTACTOEWebsite.weights_2_neurons[1], TICTACTOEWebsite.bias, TICTACTOEWebsite.weights_2_neurons[2])
        game_status_across2 = self.ActivationFunction_2_nerons(check_game_across2[0], TICTACTOEWebsite.weights_2_neurons[0], check_game_across2[1], TICTACTOEWebsite.weights_2_neurons[1], TICTACTOEWebsite.bias, TICTACTOEWebsite.weights_2_neurons[2])

        # Pass the output of 2 Neuron Neural Network as Input to 8 Neurons Neural Network for Overall Status
        TICTACTOEWebsite.FinalStatus = self.ActivationFunction_8_neurons(game_status_row1,TICTACTOEWebsite.weights_8_neurons[0],game_status_row2,TICTACTOEWebsite.weights_8_neurons[1],game_status_row3,TICTACTOEWebsite.weights_8_neurons[2],game_status_down1,TICTACTOEWebsite.weights_8_neurons[3],game_status_down2,TICTACTOEWebsite.weights_8_neurons[4],game_status_down3,TICTACTOEWebsite.weights_8_neurons[5],game_status_across1,TICTACTOEWebsite.weights_8_neurons[6],game_status_across2,TICTACTOEWebsite.weights_8_neurons[7],TICTACTOEWebsite.bias,TICTACTOEWebsite.weights_8_neurons[8])
        return TICTACTOEWebsite.FinalStatus

    @http.route('/tictactoe/website/', auth='public')
    def index(self, **kw):

        try:
            GotInput = int(http.request.params.get('input'))
        except:
            GotInput = -1

        # Tic Tac Board Status 
        if GotInput== 0:
            self.ResetGame()
        else:
            if GotInput==-500:
                self.LearnGame()
            else:            
                if GotInput == 100:
                    TICTACTOEWebsite.position=self.AutoMode(TICTACTOEWebsite.board_row1, TICTACTOEWebsite.board_row2, TICTACTOEWebsite.board_row3)
                    TICTACTOEWebsite.PlayerNumber = 2

                else:
                    TICTACTOEWebsite.position=GotInput
                    TICTACTOEWebsite.PlayerNumber = 1
                
        if TICTACTOEWebsite.position == 10:
            TICTACTOEWebsite.board_row1[0]=TICTACTOEWebsite.PlayerNumber
        if TICTACTOEWebsite.position == 11:
            TICTACTOEWebsite.board_row1[1]=TICTACTOEWebsite.PlayerNumber
        if TICTACTOEWebsite.position == 12:
            TICTACTOEWebsite.board_row1[2]=TICTACTOEWebsite.PlayerNumber
        if TICTACTOEWebsite.position == 20:
            TICTACTOEWebsite.board_row2[0]=TICTACTOEWebsite.PlayerNumber
        if TICTACTOEWebsite.position == 21:
            TICTACTOEWebsite.board_row2[1]=TICTACTOEWebsite.PlayerNumber
        if TICTACTOEWebsite.position == 22:
            TICTACTOEWebsite.board_row2[2]=TICTACTOEWebsite.PlayerNumber
        if TICTACTOEWebsite.position == 30:
            TICTACTOEWebsite.board_row3[0]=TICTACTOEWebsite.PlayerNumber
        if TICTACTOEWebsite.position == 31:
            TICTACTOEWebsite.board_row3[1]=TICTACTOEWebsite.PlayerNumber
        if TICTACTOEWebsite.position == 32:
            TICTACTOEWebsite.board_row3[2]=TICTACTOEWebsite.PlayerNumber
 
        TICTACTOEWebsite.FinalStatus = self.Check_Game_Status(TICTACTOEWebsite.board_row1,TICTACTOEWebsite.board_row2,TICTACTOEWebsite.board_row3)
        TICTACTOEWebsite.board_message=f'Game Status : {TICTACTOEWebsite.FinalStatus}'+f'Got Input : {GotInput}' +f'Player : {TICTACTOEWebsite.PlayerNumber}' +f'Bias : {TICTACTOEWebsite.bias}' 
            
        if TICTACTOEWebsite.FinalStatus == 1: 	
            TICTACTOEWebsite.board_message=f'Game Won By Player: {TICTACTOEWebsite.PlayerNumber}'   
            return http.request.render('tictactoe_module.website', {
                'board_row1': TICTACTOEWebsite.board_row1,
                'board_row2': TICTACTOEWebsite.board_row2,
                'board_row3': TICTACTOEWebsite.board_row3,            
                'board_message': TICTACTOEWebsite.board_message,            
            })

        else:
            TICTACTOEWebsite.board_message=f'Game Status : {TICTACTOEWebsite.FinalStatus}'+f'Got Input : {GotInput}'+f'Player : {TICTACTOEWebsite.PlayerNumber}'+f'Bias : {TICTACTOEWebsite.bias}'
            return http.request.render('tictactoe_module.website', {
                'board_row1': TICTACTOEWebsite.board_row1,
                'board_row2': TICTACTOEWebsite.board_row2,
                'board_row3': TICTACTOEWebsite.board_row3,            
                'board_message': TICTACTOEWebsite.board_message,            
            })

        return http.request.render('tictactoe_module.website', {
            'board_row1': TICTACTOEWebsite.board_row1,
            'board_row2': TICTACTOEWebsite.board_row2,
            'board_row3': TICTACTOEWebsite.board_row3,            
            'board_message': TICTACTOEWebsite.board_message,            
        })

