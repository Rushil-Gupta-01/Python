import random
from colorama import Fore

#Welcome message:
print("\n---------- WELCOME TO ROCK PAPER SCISSORS ----------\n\n")
print("~~~~~ INSTRUCTIONS ~~~~~")
print("Choose from:")
print("Rock🗿")
print("Paper🧻")
print('Scissors ✂')


#Variables:
computer_score = 0
player_score = 0
tie_score = 0
possibleHands = ["Rock", "Paper", "Scissors"]

#Checking for the winner:
def checkforwinner(player_hand, computer_hand):
    if(player_hand == "Rock" and computer_hand == "Paper"):
        print("\n\n=>Sorry you lost! :(")
        return "Computer"

    elif(player_hand == "Rock" and computer_hand== "Scissors"):
        print("\n\n=> Congrats! You won! :)")
        return "Player"

    elif(player_hand == "Paper" and computer_hand == "Scissors"):
        print("\n\n=>Sorry you lost! :(")
        return "Computer"

    elif(player_hand == "Paper" and computer_hand == "Rock"):
        print("\n\n=>Congrats! You won! :)")
        return "Player"

    elif(player_hand == "Scissors" and computer_hand == "Rock"):
        print("\n\n=>Sorry you lost! :(")
        return "Computer"

    elif(player_hand == "Scissors" and computer_hand == "Paper"):
        print("\n\n=>Congrats! You won! :)")
        return "Player"

    else:
        print("\n\n=>It's a tie, play again!")
        return "Tie"



#Game Loop:
while (player_score != 3 and computer_score !=3):
    while True:
       player_hand = input("\nPick a hand. Rock, Paper, or Scissors: ")
       if(player_hand == "Rock" or player_hand == "Paper" or player_hand == 'Scissors'):
        break
       else:
        print(Fore.RED + "Invalid Input. Try again.")
        print(Fore.WHITE+ "")


#Computer Pick
    computer_hand = random.choice(possibleHands)


#Printing the results:
    print("Your hand: ", player_hand)
    print("Computer hand: ", computer_hand)
    result = checkforwinner(player_hand, computer_hand)

    if (result == "Player"):
        player_score +=1
    elif(result == "Computer"):
        computer_score +=1
    else:
        tie_score +=1
    print("\n Your score: ",player_score, 
    "||""Computer Score: ", computer_score, 
    "||""Ties: ", tie_score)


print("\nGAME OVER! THANK YOU FOR PLAYING :)")
