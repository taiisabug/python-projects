c=1
while c<101: 
    if c%3==0 and c%5==0:
        print ("FizzBuzz")
        c=c+1	
    elif c%3==0:
        print ("Fizz")	
        c=c+1
    elif c%5==0:
        print ("Buzz")
        c=c+1
    else:
        print (c)
        c=c+1