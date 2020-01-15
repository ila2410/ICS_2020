
# Let's make a game of guess a number game
# At this game computer generates a number
# and a user should guess it!

#########################################
#             Ingredients:              #
#---------------------------------------#
#       from random import randint      #
#                 print()               #
#                 input()               #
#              if-elif-else             #
#                  int()                #
#########################################

# Import random module
import random


if __name__  == "__main__":

    # Print welcomming words
    print("Welcome to my game")

    # Get a number from user by input() function
    number = int(input("guess a number from 1-10"))

    # Convert the user's number to integer (as long as input() returns string)
   

    # Generate random number using randint 
    awnser = random.randint(1,10)
    # Check if user's guess equal to computer's number
    if number == awnser:
        print("you win bitch boi")
        # Print to user that the guess is right
    elif number > awnser: 
            print("too big ")

    else:
            print("too small")

    # Check if user's guess is morte than computer's number

        # Print to user that it is more


    # If it's not equal or more

        # Print that it's too small
