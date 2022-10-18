print ("Hello world!")

import time

time.sleep(1)

import sys

while True:
    cont = input("Start? yes/no ")

    while cont.lower() not in ("yes", "no"):
        cont = input("You may only select yes or no.")

    if cont == "yes":
        print("Yay!")
        break

    if cont == "no":
      sys.exit("See you next time!")

time.sleep(1) # Sleep for 1 seconds

name = input ("What is your name?")

print ("Hello ", name, ". I am catquestion.py")

time.sleep(1)

valid = False

while not valid: 
    try:
        x = int(input('How old are you?'))
        valid = True 
    except ValueError:
        print('Please only input digits.')



print ("Wow! I know someone who is ", x, " too!")

time.sleep(1)

while True:
    cont = input("Do you like cats? ")

    while cont.lower() not in ("yes", "no"):
        cont = input("You may only select yes or no.")

    if cont == "no":
        sys.exit ("We cannot be friends then. Goodbye")

    if cont == "yes":
        print ("I love cats. They are my favourite.")
        break

time.sleep (1)

while True:
    cont = input("I want to be friends. Do you want to be my friend?")

    while cont.lower() not in ("yes", "no"):
        cont = input("You may only select yes or no.")

    if cont == "no":
        import os
        os.system('shutdown -s')

    if cont == "yes":
        print ("Yay!")
        break

time.sleep(1)

print ("Ok friend. I must go now. Have a good day. Goodbye!")