import random
from colorama import Fore,Style
from Hangman_parts import parts
from time import sleep


print(Style.BRIGHT+ "\n---------- WELCOME TO HANG-MAN ----------\n")

#Options 
my_file = open('C:\\Users\\india\\OneDrive\\Desktop\\Python Udemy\\Projects\\Hangman\\words.txt', "r")
words_list = my_file.read().split('\n')


#Picking a word from the list
picked = random.choice(words_list)

right =["_"] * len(picked)
wrong = []

parts(len(wrong))
print(Style.NORMAL+ "\nLet me think of a word...")

#Storing the guess


def update():
    for i in right:
        print(i, end= ' ')
    print()
update()



def wait():
    for i in range(3):
        print('.', end = "")
        sleep(.3)
    print()
    
wait()

print("The word has", len(picked), "letters")

#Loop: Until the word is guessed:
while True:

    print(Fore.YELLOW+ '======================')
    guess = input(Fore.GREEN+ "Guess a letter: ")
    print("Let me check")
    wait()

    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index += 1
        update()

    else:
        if guess not in wrong:
            wrong.append(guess)
            parts(len(wrong))
        else:
            print("You already guessed", guess)
        print(wrong)

    if len(wrong)>5:
        print("You lost! :(")
        print("I picked", picked)
        break

    if '_' not in right:
        print('You win! :)')
        break


    














