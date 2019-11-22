import random
 
number = random.randrange(1, 26)
guesses = 0
print ("I'm thinking of a number between 1-25, you got 6 tries")

while guesses < 6:
    guess = int(input("Please enter your guess: "))
    guesses = guesses + 1
    if guess == number:
        print ("You got It!")
    elif guess < number:
        print ("Your guess is too low")
    else:
        print ("Your guess is too high")
print ("Better luck next time")