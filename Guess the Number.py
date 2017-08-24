import random

randNumber = random.randint(1,100)
print(randNumber)
guessNumber = int(input("Guess the number from 1 to 100.\n"))

while randNumber != guessNumber:

    if guessNumber > 100 or guessNumber < 1:
        print("You entered a number bigger than 100 or smaller than 1, try again:\n")
        guessNumber = int(input())
    elif randNumber > guessNumber:
        print("Too low, try again:\n")
        guessNumber = int(input())

    elif randNumber < guessNumber:
        print("Too high, try again: \n")
        guessNumber = int(input())

print("You got it! Well done.")