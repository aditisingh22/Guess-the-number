#Guess the number
# Based on a variable already present in code,user needs to guess the number,with fixed number of attempts
# Condition:
# If user inputs number greater than n(suppose the number),code prompts to lessen the guess and
#If user inputs number less than n(suppose the number),code prompts to take a larger number guess
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