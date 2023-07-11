import random
from colorama import Fore

print("\n🔵 🔵 🔵 WELCOME TO CONNECT 4 🟠 🟠 🟠\n")

#Game Board:
possibleLetters = ["A","B","C","D","E","F"]
gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]  #Row => 1 #Col =>2
rows =6
cols =7

def printgameBoard():
    print("\n     A    B    C    D    E    F  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(6):
            if(gameBoard[x][y] == "🔵"):
                print("",gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "🟠"):
             print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+")

    
def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(token):
  ### Check horizontal spaces
  for y in range(rows):
    for x in range(cols - 4):
      if gameBoard[x][y] == token and gameBoard[x+1][y] == token and gameBoard[x+2][y] == token and gameBoard[x+3][y] == token :
        print(Fore.GREEN+ "\n=> Game over", token, "wins! Thank you for playing :)")
        return True

  ### Check vertical spaces
  for x in range(rows):
    for y in range(cols - 4):
      if gameBoard[x][y] == token and gameBoard[x][y+1] == token and gameBoard[x][y+2]== token and gameBoard[x][y+3]==token :
        print(Fore.GREEN+ "\n=>Game over", token, "wins! Thank you for playing :)")
        return True

  ### Check upper right to bottom left diagonal spaces
  for x in range(rows - 4):
    for y in range(4, cols):
      if gameBoard[x][y] == token and gameBoard[x+1][y-1] == token and gameBoard[x+2][y-2] == token and gameBoard[x+3][y-3] == token:
        print("\nGame over", token, "wins! Thank you for playing :)")
        return True

  ### Check upper left to bottom right diagonal spaces
  for x in range(rows - 3):
    for y in range(cols - 3):
      if gameBoard[x][y] == token and gameBoard[x+1][y+1] == token and gameBoard[x+2][y+2] == token and gameBoard[x+3][y+3] == token:
        print("\nGame over", token, "wins! Thank you for playing :)")
        return True
  return False


def coordinatePasser(inputString):
    coordinate = [None]*2
    if(inputString[0] == "A"):
        coordinate[1] = 0
    elif(inputString[0] == "B"):
        coordinate[1] = 1 
    elif(inputString[0] == "C"):
        coordinate[1] = 2 
    elif(inputString[0] == "D"):
        coordinate[1] = 3 
    elif(inputString[0] == "E"):
        coordinate[1] = 4 
    elif(inputString[0] == "F"):
        coordinate[1] = 5 
    #elif(inputString[0] == "G"):
        #coordinate[1] = 6
    else:
        print("Invalid")
    coordinate[0] = int(inputString[1])
    return coordinate

def is_space_available(allottedCoordinate):
    if(gameBoard[allottedCoordinate[0]][allottedCoordinate[1]] == "🟠"):
        return False
    elif(gameBoard[allottedCoordinate[0]][allottedCoordinate[1]] == "🔵"):
        return False
    else: 
        return True

def gravity_checker(allottedCoordinate):
    #CAlculate Space Below:
    spaceBelow = [None] * 2
    spaceBelow[0] = allottedCoordinate[0] + 1
    spaceBelow[1] = allottedCoordinate[1]

    #Coordinate at the bottom:
    if (spaceBelow[0]== 6):
            return True
    
    #Check if there is token below:
    if(is_space_available(spaceBelow)==False):
        return True
    return False

leaveLoop = False
turnCounter = 0
while(leaveLoop == False):
    if(turnCounter % 2 ==0):
        printgameBoard()
        while True:
            space_picked = input("\n=>Choose a space: ")
            coordinate = coordinatePasser(space_picked)
            try:
                if(is_space_available(coordinate) and gravity_checker(coordinate)):
                    modifyArray(coordinate, '🔵')
                    break
                else:
                    print("Not a valid coordinate!")

            except:
                print("Error occured! Please try again :(")
        winner = checkForWinner('🔵')
        turnCounter +=1

    else:
        while True:
            computer_choice = [random.choice(possibleLetters), random.randint(0,5)]
            computer_coordinate = coordinatePasser(computer_choice)
            if(is_space_available(computer_coordinate) and gravity_checker(computer_coordinate)):
                modifyArray(computer_coordinate, '🟠')
                break
        turnCounter +=1
        winner = checkForWinner('🟠')
        
    if(winner):
        printgameBoard()
        break
