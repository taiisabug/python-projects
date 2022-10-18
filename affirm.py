import random
import sys
import time

AFFIRM = ("You are worthy of what you desire!", "You can and you will!", "You are enough.", "Your challenges are actually opportunities!", "You are beautiful just the way you are :>",  "Asking for help is a sign of self-respect and self-awareness!", "Changing your mind is a strength, not a weakness!", "You are allowed to feel good!", "You are loved and you are worthy!", "You are valued and are helpful!", "You belong here, and you deserve to take up space!", "You deserve respect and love.", "You do not need to linger in dark places; there is help for you!", "You have everything you need to suceed.", "You nourish yourself with kind words and joyful foods.", "You strive for joy, not perfection.")

print ("Hello! I hope you are doing well today :D")

time.sleep(1)

while True:
    cont = input("Would you like an affirmation? yes/no ")

    while cont.lower() not in ("yes", "no"):
        cont = input("Sorry! But you may only choose yes or no.")

    if cont == "yes":
        affirmation = random.choice(AFFIRM)
        print("Your affirmation is:")
        time.sleep(1)
        print (affirmation)
        flag = 1
        time.sleep(1)
        break

    if cont == "no":
      print ("See you next time!")
      flag = 2
      break

time.sleep (1)

while True and flag == 1:
    cont = input("Would you like another one? yes/no ")

    while cont.lower() not in ("yes", "no"):
        cont = input("Sorry! But you may only choose yes or no.")

    if cont == "yes":
        affirmation = random.choice(AFFIRM) 
        print("Your affirmation is:")
        time.sleep(1)
        print (affirmation)
        flag = 1
        time.sleep(1)

    if cont == "no":
     break


if flag == 1:
  print ("See you next time!")
  sys.exit

