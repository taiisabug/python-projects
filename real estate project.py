
fagent = input ("Please enter the first agent:\t")
while len(fagent) > 20:
    fagent = input ("You are limited to 20 characters. Please re-input the agent name:\t")

fsp = int(input("Please input the sale price that %s sold at:\t" %fagent))
while fsp > 10000000:
    fsp = int(input ("Price must be lower than 10'000'000. Please re-input the price:\t"))
    
sagent = input ("Please enter the second agent:\t")
while len(sagent) > 20:
    sagent = input ("You are limited to 20 characters. Please re-input the agent name:\t")

ssp = int(input("Please input the sale price that %s sold at:\t" %sagent))
while ssp > 10000000:
    ssp = int(input ("Price must be lower than 10'000'000. Please re-input the price:\t"))

tagent = input ("Please enter the third agent:\t")
while len(tagent) > 20:
    tagent = input ("You are limited to 20 characters. Please re-input the agent name:\t")

tsp = int(input("Please input the sale price that %s sold at:\t" %tagent))
while tsp > 10000000:
    tsp = int(input ("Price must be lower than 10'000'000. Please re-input the price:\t\n\n"))
    
time.sleep (1)

#Display in a table form all of the information with headings of Agent, Price and Commission.
#Information is expected to be formatted!!!!  Names of agents are left justified.  Price and commission are right justified.  

#Output should look as follows:
#Agent			  Price			Commission
#Smith			  875000		21875.00
#Jones			  1125000		28125.00
#Khan			  520000		13000.00

com1 = fsp*0.025
com2 = ssp*0.025
com3 = tsp*0.025
a = ("Agent")
b = ("Price")
c = ("Commission")

print ("\n\n%-10s%10s%20s" %(a,b,c))
print ("%-10s%10i$%20.2f$" %(fagent, fsp, com1))
print ("%-10s%10i$%20.2$f" %(sagent, ssp, com2))
print ("%-10s%10i$%20.2f$" %(tagent, tsp, com3))