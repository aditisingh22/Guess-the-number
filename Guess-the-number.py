
print("WELCOME TO GUESS THE NUMBER")
print("="*27)
n=15
g=0
while(n==15):
    if (g<4):
        g=g+1
        i=int(input("Guess the number"))
        print("This was attempt number",g,",",5-g,"remaining")
        if (i<n):
            print("Try a greater number")
        elif (i>n):
            print("Try a smaller number as input")
        elif (i==n):
            print("Congrats,that was a successful attempt")
            break
    else:
        print("Sorry, too many trials,the number was",n)
        break
