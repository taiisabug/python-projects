from random import *
import time
again = True
colors = ["R", "O", "Y", "G", "B", "P"]
round = 1

print ("Welcome to Mastermind. \nYour colour choices are 'R' (red), 'O' (orange), 'Y' (yellow), 'G' (green), 'B' (blue), and 'P' (purple). \nYou have 8 tries! Good luck.")

while again == True:
    shuffle(colors)
    order = colors[:4]
    #print (order)
    enter = []
    counterend = 8
    countertry = 0
    counterspot = 0
    
    while enter != order:
        
        enter = input("What is your guess? ")
        enter = list(enter)
        counterend -= 1
        countertry += 1
        counterspot = 0
        if enter == order:
            if countertry == 1:
                print ("You won!! In ", countertry, " attempt!! Good Job :D")
            else:
                print ("You won!! In ", countertry, " attempts!! Good Job :D")            
            break
        if counterend == 0:
            print ("You ran out of attempts! The answer was ", str(order))
            break    
        for i in range(4):
            if enter[i] == order[i]:
                counterspot += 1
        if counterend == 1:
            print ("You are wrong with ", counterspot, " colours in the right spot. \nYou have ", counterend, " attempt left. Make it count.")
        else:
            print ("You are wrong with ", counterspot, " colours in the right spot. \nYou have ", counterend, " attempts left.")
        
    play = input("Do you want to play again? <yes or no>   ")
    if play == ("yes"):
        round += 1
        print ("Here we go!! Round " +str(round) + "!!!")
    else:
        print ("Ok! See you next time :D")
        again = False
