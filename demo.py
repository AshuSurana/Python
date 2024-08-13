#A simple command line game, Number Guessing
import random

digits=list(range(10))
random.shuffle(digits)
comp_digits=(digits[:3])
print("Computers 3 digits/Guess",comp_digits)

i=0
while i<5:

    guess=(input("What is yor guess? 3 digit number: "))
    user_guess=list(map(int,guess.split(" ")))  #converting string input(list of string) to list of ints
    print(user_guess)

    if comp_digits==user_guess:
        print("Match: You've guessed a correct number in the correct position")
        break
    else:
        comp_digit=comp_digits.copy()
        comp_digit.sort()
        user_guess.sort()
        if comp_digit==user_guess:
            print("Close: You've guessed a correct number but in the wrong position")
        else:
            print("Nope:You haven't guess any of the numbers correctly")
    i=i+1



    
    
