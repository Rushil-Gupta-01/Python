from colorama import Fore


def game_instructions():
    #Welcome Message:
    print(Fore.LIGHTYELLOW_EX+ "\n✖ ✖ ✖   WELCOME TO TIC TAC TOE O O O\n")
    print(Fore.WHITE + (""))
game_instructions()


#Players:
Player1 = input("Player 1: ")
Player2 = input("\nPlayer 2: ")
print()

print(Player1,': ✖')
print(Player2,': O')

    



#Variables:
possiblePositions = [1,2,3,4,5,6,7,8,9]
game_board = [['1️⃣ ','2️⃣ ','3️⃣ '], ['4️⃣ ','5️⃣ ','6️⃣ '], ['7️⃣ ','8️⃣ ','9️⃣ ']]
rows = 3
cols = 3

#Printing the game_board:
def printgame_board():
    for x in range(rows):
        print("\n+-----+-----+-----+")
        print('|', end="")
        for y in range(cols):
            print("",game_board[x][y], end= '  |')
    print("\n+-----+-----+-----+\n")




#ModifyArray:
def modifyArray(num, turn):
    num -=1
    if(num == 0):
        game_board[0][0] = turn
    elif(num == 1):
        game_board[0][1] = turn
    elif(num == 2):
        game_board[0][2] = turn
    elif(num == 3):
        game_board[1][0] = turn
    elif(num == 4):
        game_board[1][1] = turn
    elif(num == 5):
        game_board[1][2] = turn
    elif(num == 6):
        game_board[2][0] = turn
    elif(num == 7):
        game_board[2][1] = turn
    elif (num == 8):
        game_board[2][2] = turn

  
#Checking for the winner
def checkforwinner(game_board):
     #//X-Axis
    if(game_board[0][0] == '🟡' and game_board[0][1] == '🟡' and game_board[0][2] == '🟡'):
        print("\n🟡 has won!")
        return "🟡"
    elif (game_board[0][0] == '🟠' and game_board[0][1] == '🟠' and game_board[0][2] == '🟠'):
        print("\n🟠 has won!")
        return "🟠"
    elif (game_board[1][0] == '🟡' and game_board[1][1] == '🟡' and game_board[1][2] == '🟡'):
        print("\n🟡 has won!")
        return "🟡"
    elif (game_board[1][0] == '🟠' and game_board[1][1] == '🟠' and game_board[1][2] == '🟠'):
        print("\n🟠 has won!")
        return "🟠"
    elif (game_board[2][0] == '🟡' and game_board[2][1] == '🟡' and game_board[2][2] == '🟡'):
        print("\n🟡 has won!")
        return "🟡"
    elif (game_board[2][0] == '🟠' and game_board[2][1] == '🟠' and game_board[2][2] == '🟠'):
        print("\n🟠 has won!")
        return "🟠"


    #//Y-Axis
    if(game_board[0][0] == '🟡' and game_board[1][0] == '🟡' and game_board[2][0] == '🟡'):
        print("\n🟡 has won!")
        return "🟡"
    elif(game_board[0][0] == '🟡' and game_board[1][0] == '🟡' and game_board[2][0] == '🟡'):
        print("\n🟡 has won!")
        return "🟡"
    elif(game_board[0][1] == '🟡' and game_board[1][1] == '🟡' and game_board[2][1] == '🟡'):
        print("\n🟡 has won!")
        return "🟡"
    elif(game_board[0][1] == '🟠' and game_board[1][1] == '🟠' and game_board[2][1] == '🟠'):
        print("\n🟠 has won!")
        return "🟠"
    elif(game_board[0][2] == '🟡' and game_board[1][2] == '🟡' and game_board[2][2] == '🟡'):
        print("\n\n🟡 has won!")
        return "🟡"
    elif(game_board[0][2] == '🟠' and game_board[1][2] == '🟠' and game_board[2][2] == '🟠'):
        print("\n🟠 has won!")
        return "🟠"


    #Cross Axis or diagnal Axis:
    if(game_board[0][0] == '🟡' and game_board[1][1] == '🟡' and game_board[2][2] == '🟡'):
        print("\n🟡 has won!")
        return "🟡"
    elif(game_board[0][0] == '🟠' and game_board[1][1] == '🟠' and game_board[2][2] == '🟠'):
        print("\n🟠 has won!")
        return "🟠"
    elif(game_board[0][2] == '🟡' and game_board[1][1] == '🟡' and game_board[2][0] == '🟡'):
        print("\n🟡 has won!")
        return "🟡"   
    elif(game_board[0][2] == '🟠' and game_board[1][1] == '🟠' and game_board[2][0] == '🟠'):
        print("\n🟠 has won!")
        return "🟠"    
    
    else:
        return 'N'

leaveloop = False
turn_counter = 0

while(leaveloop == False):
    #Player1 Turn:
    if (turn_counter %2 == 0):
        printgame_board()
        player1_choice = int(input("\n=>Player 1 choose a number (1-9): "))
        if (player1_choice >=1 or player1_choice <=9):
            modifyArray(player1_choice, '🟡' )
            possiblePositions.remove(player1_choice)
        else:
            print("Invalid input. Please try again.")
        turn_counter +=1

    #Player2 Turn:
    else:
        while(True):
            printgame_board()
            player2_choice = int(input("\n=>Player 2 choose a numer (1-9): "))
            if (player2_choice in possiblePositions):
                modifyArray(player2_choice, '🟠')
                possiblePositions.remove(player2_choice)
                turn_counter +=1
                break

    

#Checking the winner:
    winner  = checkforwinner(game_board)
    if(winner != 'N'):
        print(Fore.GREEN+ "=>GAME OVER! THANK YOU FOR PLAYING :)")
        printgame_board()
        break