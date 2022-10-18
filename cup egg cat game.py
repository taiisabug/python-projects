import random
import sys
import time

print ("Welcome to guess.py")

time.sleep (2)

print ("\nThree cups will be presented in front of you.")

time.sleep (2)

print ("\nOne will be randomly selected and will have a cat under it.")

time.sleep (2)

print ("\nIf you select the empty cup, the game will end.")
       
time.sleep(1)

cont = input("\nReady?   ")

while True:
    
    if cont not in ("yes", "no"):
        cont = input("Please select yes or no.")

    if cont == "yes":
        flag = 1
        CUPS = (1, 2, 3)
        cup = random.choice (CUPS)        
        
        while flag == 1:
            cont = int (input("Cup 1\t Cup 2\t Cup 3\t"))
            
            while not (1, 2, 3):
                cont = input("Please type only 1, 2 or 3.")    
            
            if cont == (cup):
                print ("You have selected the cup with the cat!")
                print ("|\---/| \n| o_o | \n \_^_/")
                time.sleep (1)
                print ("\n")
                cont = input ("Play again?")
                break
            
            else:
                print ("Nice try! You selected the wrong cup.")
                time.sleep (1)
                print ("\n")
                print ("Play again?")
                break                
        

    if cont == "no":
        time.sleep (2)
        print ("\nSee you next time!")
        flag = 3
        break
    



