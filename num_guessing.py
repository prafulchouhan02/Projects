import random

guess = 0
number = random.randint(1,100)

while guess != number:
    guess = int(input("Enter Guess:  "))

    if guess > number :
        print("Your Guess Is Greater Then Number ")
    elif guess < number :
        print("Your Guess Is Lower Then Number ")
    else:
        print(" You Won ")
