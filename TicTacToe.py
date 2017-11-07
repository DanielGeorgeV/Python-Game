'''
Created on Oct 24, 2017

@author: Daniel George Valsarajan
'''

from __future__ import print_function
from time import sleep
from Game.CPU_TicTacToe import Brain

class TicTacToe(object):
    '''
    TicTacToe game assignment from python lecture in udemey course
    '''
    gameTable = {0:[' ',' ',' '],1:[' ',' ',' '],2:[' ',' ',' ']}

    def display_board(self,gameTable):
        print("X O game")
        print("| ",gameTable[2]," |")
        print("| ",gameTable[1]," |")
        print("| ",gameTable[0]," |")
        
    def xLocation(self, location, gameTable):
        print("Specify X location")
        if location in (7,8,9):
            if location == 8:
                gameTable[2][1] = 'X'
            elif location == 7:
                gameTable[2][0] = 'X'
            else:
                gameTable[2][2] = 'X'
        elif location in (4,5,6):
            if location == 5:
                gameTable[1][1] = 'X'
            elif location == 4:
                gameTable[1][0] = 'X'
            else:
                gameTable[1][2] = 'X'
        elif location in (1,2,3):
            if location == 2:
                gameTable[0][1] = 'X'
            elif location == 1:
                gameTable[0][0] = 'X'
            else:
                gameTable[0][2] = 'X'
        else:
            print("Invalid location")
        return gameTable
    
    def oLocation(self, location, gameTable):
        print("Specify O location")
        if(location in range(7, 10)):
            if(location == 8):
                gameTable[2][1] = 'O'
            elif(location == 7):
                gameTable[2][0] = 'O'
            else:
                gameTable[2][2] = 'O'
        elif(location in range(4, 7)):
            if(location == 5):
                gameTable[1][1] = 'O'
            elif(location == 4):
                gameTable[1][0] = 'O'
            else:
                gameTable[1][2] = 'O'
        elif(location in range(1, 4)):
            if(location == 2):
                gameTable[0][1] = 'O'
            elif(location == 1):
                gameTable[0][0] = 'O'
            else:
                gameTable[0][2] = 'O'
        else:
            print("Invalid location")
        return gameTable
        
    def checkRewrite(self, location, gameTable):
        if(location in range(7, 10)):
            if(location == 8):
                if(gameTable[2][1] == 'O' or gameTable[2][1] == 'X'):
                    return False
                else:
                    return True
            elif(location == 7):
                if(gameTable[2][0] == 'O' or gameTable[2][0] == 'X'):
                    return False
                else:
                    return True
            else:
                if(gameTable[2][2] == 'O' or gameTable[2][2] == 'X'):
                    return False
                else:
                    return True
        elif(location in range(4, 7)):
            if(location == 5):
                if(gameTable[1][1] == 'O' or gameTable[1][1] == 'X'):
                    return False
                else:
                    return True
            elif(location == 4):
                if(gameTable[1][0] == 'O' or gameTable[1][0] == 'X'):
                    return False
                else:
                    return True
            else:
                if(gameTable[1][2] == 'O' or gameTable[1][2] == 'X'):
                    return False
                else:
                    return True
        elif(location in range(1, 4)):
            if(location == 2):
                if(gameTable[0][1] == 'O' or gameTable[0][1] == 'X'):
                    return False
                else:
                    return True
            elif(location == 1):
                if(gameTable[0][0] == 'O') or (gameTable[0][0] == 'X'):
                    return False
                else:
                    return True
            elif(location==3):
                if(gameTable[0][2] == 'O') or (gameTable[0][2] == 'X'):
                    return False
                else:
                    return True
    def winner(self, gameTable):
        options = ['X','O']
        global flag
        for option in options:
            if(gameTable[0][0] == option and gameTable[0][1] == option and gameTable[0][2] == option):
                return True
            elif(gameTable[1][0] == option and gameTable[1][1] == option and gameTable[1][2] == option):
                return True
            elif(gameTable[2][0] == option and gameTable[2][1] == option and gameTable[2][2] == option):
                return True
            elif(gameTable[0][0] == option and gameTable[1][0] == option and gameTable[2][0] == option):
                return True
            elif(gameTable[0][1] == option and gameTable[1][1] == option and gameTable[2][1] == option):
                return True
            elif(gameTable[0][2] == option and gameTable[1][2] == option and gameTable[2][2] == option):
                return True
            elif(gameTable[0][0] == option and gameTable[1][1] == option and gameTable[2][2] == option):
                return True
            elif(gameTable[0][2] == option and gameTable[1][1] == option and gameTable[2][0] == option):
                return True
            else:
                flag = False
        return flag
ttt = TicTacToe()
print("Start the game")
print("Press 1 for 1-Player game & 2 for 2-Players game")
player = int(raw_input())
if (player==1):
    cpu = Brain()
    print("Player is X & CPU is O")
    global i
    i = 1
    gameTable = ttt.gameTable
    while(i < 10):
        ttt.display_board(gameTable)
        if(i % 2 == 0):
            print("CPU is thinking...")
            sleep(1)
            location = cpu.Cerebrum(gameTable, 'O')
            flag = ttt.checkRewrite(location,gameTable)
            if(flag==True):
                gameTable = ttt.oLocation(location,gameTable)
            else:
                print("Enter proper location")
                i=i-2
        else:
            print("Specify X location")
            location = int(raw_input())
            flag = ttt.checkRewrite(location,gameTable)
            if(flag==True):
                gameTable = ttt.xLocation(location,gameTable)
            else:
                print("Enter proper location")
                i=i-2
        flag = ttt.winner(gameTable)
        if(flag==False):
            i=i+1
            continue
        else:
            if(i%2==0):
                print("Winner is O")
                ttt.display_board(gameTable)
            else:
                print("Winner is X")
                ttt.display_board(gameTable)
            break
    ttt.display_board(gameTable)
    if(i>9):
        print("Game Over")
    
elif (player==2):
    global i
    i = 1
    gameTable = ttt.gameTable
    while(i < 10):
        ttt.display_board(gameTable)
        if(i % 2 == 0):
            print("Specify O location")
            location = int(raw_input())
            flag = ttt.checkRewrite(location,gameTable)
            if(flag==True):
                gameTable = ttt.oLocation(location,gameTable)
            else:
                print("Enter proper location")
                i=i-2
        else:
            print("Specify X location")
            location = int(raw_input())
            flag = ttt.checkRewrite(location,gameTable)
            if(flag==True):
                gameTable = ttt.xLocation(location,gameTable)
            else:
                print("Enter proper location")
                i=i-2
        flag = ttt.winner(gameTable)
        if(flag==False):
            i=i+1
            continue
        else:
            if(i%2==0):
                print("Winner is O")
                ttt.display_board(gameTable)
            else:
                print("Winner is X")
                ttt.display_board(gameTable)
            break
    ttt.display_board(gameTable)
    if(i>9):
        print("Game Over")
