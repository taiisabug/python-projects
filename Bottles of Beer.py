b=99
while b>1:
    print (b,"bottles of beer on the wall,",b,"bottles of beer.")
    b=b-1
    if b>1:
        print ("Take one down and pass it around,",b,"bottles of beer on the wall.\n")
    else:
        print ("Take one down and pass it around,",b,"bottle of beer on the wall.\n")
if b==1:
    print (b,"bottle of beer on the wall,",b,"bottle of beer.")
    b=b-1
    print ("Take one down and pass it around, no more bottles of beer on the wall.\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")