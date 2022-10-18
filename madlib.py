import sys, time 

txt = ("Welcome to madlib.py\n\nStory from https://www.madtakes.com/libs/176.html\n\nWhen prompted, please enter noun, adjective or item.\n\nEnjoy!\n\n\n")

for char in txt: 
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.05) 
    
time.sleep (1)

colour = input("Please input a colour :\t")
superlative = input("Please input a superlative (word ending in est) :\t")
adjective = input("Please input an adjective :\t")
bodypartP = input("Please input a plural body part :\t")
bodypart = input("Please input a body part :\t")
noun = input("Please input a noun :\t")
animalP = input("Please input a plural animal :\t")
adj1 = input("Please input an adjective :\t")
adj2 = input("Please input an adjective :\t")
adj3 = input("Please input an adjective :\t")

time.sleep (1)

story = ("\n\nThe ", colour, " Dragon is the ", superlative, " Dragon of all.\nIt has ", adjective," ", bodypartP,", and a ", bodypart," shaped like a ",noun, ".\nIt loves to eat ", animalP,", although it will feast on nearly anything.\nIt is ", adj1," and ", adj2,".\nYou must be ", adj3," around it, or you may end up as it`s meal!\n\n")

STORY = story

for char in STORY: 
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.25) 
    
time.sleep (1)

thanks = ("Thank you for playing!")

for char in thanks: 
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.05) 