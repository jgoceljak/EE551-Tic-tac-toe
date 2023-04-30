# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:15:58 2023

@author: kingo
"""
import random
import math



player1Score = 0
player2Score = 0
winner = 0
isWinner = False

def main():
    
    start = input("Enter 0 to start playing\n")
    while start != "0":
        start =  input("Enter 0 to start playing\n")
    if start == "0":
        initialize()
    
        
def initialize():
   global board
   global currentTurn
   global winner
   global isWinner
   winner = 0
   isWinner = False
   board = [["□","□","□"], #Initialize Board
            ["□","□","□"],
            ["□","□","□"]]
   a = random.randint(0,1)  #Randomly choose first player
   if a == 1:
       currentTurn = 1
       print("Player 1 Will go first")
   else:
       currentTurn = 2
       print("Player 2 Will go first")
   game()
       
def displayBoard():
    
    print("GAME BOARD\n")
    for x in range(3):
        print(board[x][0] + "  " + board[x][1] + "  " + board[x][2]) #Shows Board 
        print("\n")
  
def checkWinner():

    for x in range(3): #check verticals
        if board[0][x] == 'X' and board[1][x] == 'X' and board[2][x] == 'X':
            winner = 1
            isWinner = True
            return winner
        elif board[0][x] == 'O' and board[1][x] == 'O' and board[2][x] == 'O':
            winner = 2
            isWinner = True
            return winner
            
    for x in range(3): #check horizontals
        if board[x][0] == board[x][1] == board[x][2] == 'X':
            winner = 1
            isWinner = True
            return winner
        elif board[x][0] == board[x][1] == board[x][2] == 'O':
            winner = 2
            isWinner = True
            return winner
        
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        winner = 1
        return winner
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        winner = 2
        return winner
    
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        winner = 1
        return winner
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        winner = 2
        return winner
    
def game():
    global currentTurn
    global player1Score
    global player2Score
    global board
    validSpace = False
    while isWinner == False: #Loop Game alternating players until there is a winner
        validSpace = False
        winner = checkWinner()
        if winner == 1 or winner == 2:
            isWinner == True
            displayBoard()
            print("Player " + str(winner) + " has won!\n")
            if winner == 1:
                player1Score += 1
            elif winner == 2:
                player2Score += 2
            reset = input("Press 0 to restart the game, or 1 to reset everything\n")
            while reset != "0" and reset != "1":
                reset =  input("Press 0 to restart the game, or 1 to reset everything\n")
            if reset == "0":
                print("Resetting Game Board\n")
                initialize()
            elif reset == "1":
                reset()
        if currentTurn == 1:
            print("Player 1 Go\n")
        else:
            print("Player 2 Go\n")
        displayBoard()    
        while validSpace == False:
            row = input("Player " + str(currentTurn) + ", choose a row from 1 to 3\n")
            while row != "1" and row != "2" and row != "3":
                row = input("Invalid input, input either 1, 2, or 3\n")
            column = input("Player " + str(currentTurn) + ", now choose a column from 1 to 3\n")
            while column != "1" and column != "2" and column != "3":
                column = input("Invalid input, input either 1, 2, or 3\n")
            if board[int(row)-1][int(column)-1] != "□":
                print("That position is already occupied!")
            else:
                validSpace = True
        if currentTurn ==  1:
            board[int(row)-1][int(column)-1] = "X"
        elif currentTurn == 2:
            board[int(row)-1][int(column)-1] = "O"
        if currentTurn == 1:
            currentTurn = 2
        else:
            currentTurn= 1
        
        
        
        
        
main()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            
        