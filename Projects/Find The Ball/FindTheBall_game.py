from random import shuffle
#Shuffling the list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

gamelist = ['','O','']
shuffle_list(gamelist)

#Accepting user input
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Pick a number: 0,1,2 ')
    return int(guess)

#Checking the user input
def check_list(mylist,guess):
    if mylist[guess] == 'O':
        print("=> Correct!!")
    else:
        print("=> Wrong Guess!!")
        print(mylist)


#Initial List
mylist = ['','O','']

#Shuffled List
mixedup_list = shuffle_list(mylist)

#User Guess
guess = player_guess()

#Checking the answer
check_list(mixedup_list,guess)
