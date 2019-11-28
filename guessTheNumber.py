import random

hiddenNum = random.randrange(1,50)

guess = int(input("Guess and enter the number between 1 to 50: "))

if guess == hiddenNum:
    print("You won!")
elif guess < hiddenNum:
    print("Your guess is low")
else:
    print("Your guess is high")
