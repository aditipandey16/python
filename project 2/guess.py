import random
randnumber=random.randint(1,100)
#print(randnumber)
userGuess=None
guesses=0
while(userGuess!=randnumber):
    userGuess=int(input("Enter your guess: "))
    guesses+=1
    if(userGuess==randnumber):
        print("You guessed it right")
    else:
        if(userGuess>randnumber):
            print("You Guessed it Wrong! Enter a smaller Number")
        else:
            print("You Guessed it Wrong! Enter a larger Number")
print("You guessed the number in ",guesses,"guesses")
    