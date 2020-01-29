import random

print("Welcome to the number guessing game!")

guess = input("Please guess the number between 0 and 19: ")
guess_int = int(guess)
the_number = random.randrange(20)

if guess_int == the_number:
    print("You are correct!")
elif guess_int > the_number:
    print("Your guess was too high")
else:
    print("Your guess was too low")