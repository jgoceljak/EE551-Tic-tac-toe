# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:15:58 2023

@author: kingo
"""
import random
import math


currentTurn = 0
winner = False
player1Score = 0
player2Score = 0

def main():

    start = input("Enter 0 to start playing\n")
    while start != "0":
        start =  input("Enter 0 to start playing\n")
    if start == "0":
        initialize()
    
        
def initialize():
   global board
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
  
def checkWiner():
        
    
def game():
    while winner == False: #Loop Game alternating players until there is a winner
        if currentTurn == 1:
            print("Player 1 Go\n")
        else:
            print("Player 2 Go\n")
        displayBoard()    
        
main()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            
        