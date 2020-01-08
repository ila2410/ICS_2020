
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

    # Print welcoming words
    print("welcome to the game, you sucks!")

    # Generate random number using randint
    random_number =  random.randint(1, 100)

    # using the while loop to setup for 'try-except' error handling
    while(True):
        
        try:
            # Get a number from user by input() function, at the same time
            # Convert the user's number to integer (as long as input() returns string)
            number = int(input("guess a number here (from 1 to 100) -> "))
            
            # I was thinking to use this to prevent user from inputting a number below or above the range
            # if number > 100:
            #     print("sorry your number is more than 100! pick another number less than 100")
            # elif number < 1:
            #     print("sorry your number is less than 1! pick another number more or equal than one")
            
            # Check if user's guess equal to computer's number
            if number == random_number:
                # Print to user that the guess is right
                print("your guess is right!")
            
            # Check if user's guess is more than computer's number
            elif number > random_number:
                # Print to user that it is more
                print("your guess is more than the actual number")
            
            # If it's not equal or more
            else:
                # Print that it's too small
                print("your guess is less than the actual number")
            break
        
        # in case the the input from user can't be converted into integer
        except ValueError:
            print("don't be cheeky!")
