import random
from colorama import Fore, Back, Style


def print_instructions():
    print(Fore.BLUE+"\n----- WELCOME TO TIC TAC TOE -----\n")
    player= input("Player Name: ")
    print("\n   ❕ Instructions ❕  ")
    print(player,": ❌")
    print("Computer:⭕")
   
print_instructions()

#variables:
possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameboard= [[1,2,3], [4,5,6], [7,8,9]] #2 arrays
rows = 3
columns = 3


#Printing the game board:
def printgameboard():
    for x in range(rows):
        print(Fore.YELLOW+"\n+---+---+---+")
        print('|', end = "")
        for y in range(columns):
            print("",gameboard[x][y], end=' |')
    print("\n+---+---+---+")


def modifyArray(num, turn):
    num -= 1
    if(num == 0):
        gameboard[0][0] = turn
    elif(num == 1):
        gameboard[0][1] = turn
    elif(num == 2):
        gameboard[0][2] = turn
    elif(num == 3):
        gameboard[1][0] = turn
    elif(num == 4):
        gameboard[1][1] = turn
    elif(num == 5):
        gameboard[1][2] = turn
    elif(num == 6):
        gameboard[2][0] = turn
    elif(num == 7):
        gameboard[2][1] = turn
    elif (num == 8):
        gameboard[2][2] = turn

#Checking for winner
def checkforwinner(gameboard):
    #//X-Axis
    if(gameboard[0][0] == 'X' and gameboard[0][1] == 'X' and gameboard[0][2] == 'X'):
        print("X has won!")
        return "X"
    elif (gameboard[0][0] == 'O' and gameboard[0][1] == 'O' and gameboard[0][2] == 'O'):
        print("O has won!")
        return "O"
    elif (gameboard[1][0] == 'X' and gameboard[1][1] == 'X' and gameboard[1][2] == 'X'):
        print("X has won!")
        return "X"
    elif (gameboard[1][0] == 'O' and gameboard[1][1] == 'O' and gameboard[1][2] == 'O'):
        print("O has won!")
        return "O"
    elif (gameboard[2][0] == 'X' and gameboard[2][1] == 'X' and gameboard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif (gameboard[2][0] == 'O' and gameboard[2][1] == 'O' and gameboard[2][2] == 'O'):
        print("O has won!")
        return "O"


    #//Y-Axis
    if(gameboard[0][0] == 'X' and gameboard[1][0] == 'X' and gameboard[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif(gameboard[0][0] == 'X' and gameboard[1][0] == 'X' and gameboard[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif(gameboard[0][1] == 'X' and gameboard[1][1] == 'X' and gameboard[2][1] == 'X'):
        print("X has won!")
        return "X"
    elif(gameboard[0][1] == 'O' and gameboard[1][1] == 'O' and gameboard[2][1] == 'O'):
        print("O has won!")
        return "O"
    elif(gameboard[0][2] == 'X' and gameboard[1][2] == 'X' and gameboard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameboard[0][2] == 'O' and gameboard[1][2] == 'O' and gameboard[2][2] == 'O'):
        print("O has won!")
        return "O"


    #Cross Axis or diagnal Axis:
    if(gameboard[0][0] == 'X' and gameboard[1][1] == 'X' and gameboard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameboard[0][0] == 'O' and gameboard[1][1] == 'O' and gameboard[2][2] == 'O'):
        print("O has won!")
        return "O"
    elif(gameboard[0][2] == 'X' and gameboard[1][1] == 'X' and gameboard[2][0] == 'X'):
        print("X has won!")
        return "X"   
    elif(gameboard[0][2] == 'O' and gameboard[1][1] == 'O' and gameboard[2][0] == 'O'):
        print("O has won!")
        return "O"    
    
    else:
        return 'N'

leaveLoop = False
turnCounter = 0

while (leaveLoop == False):
    #Player Turn:
    if (turnCounter%2==0):
        printgameboard()
        numberpicked = int(input("\nChoose a number [1-9]: "))
        if(numberpicked>=1 or numberpicked <=9):
            modifyArray(numberpicked,'X')
            possibleNumbers.remove(numberpicked)
        else:
            print("Invalid input. Please try again.")
        turnCounter += 1

        
    #Computer's Turn
    else:
        while(True):
            Computer_Choice = random.choice(possibleNumbers)
            print("\n=> Computer choice: ", Computer_Choice)
            if(Computer_Choice in possibleNumbers):
                modifyArray(Computer_Choice, 'O')
                possibleNumbers.remove(Computer_Choice)
                turnCounter += 1
                break


#Checking the winner:
    winner = checkforwinner(gameboard)
    if(winner != "N"):
        print("\nGame over! Thank you for playing :)")
        break