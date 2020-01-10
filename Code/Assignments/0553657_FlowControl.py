
# Aapo Tommila - 0553657
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
from random import randint

if __name__  == "__main__":

    # Print welcomming words
    print('Let\'s play guess a number game')

    # Get a number from user by input() function
    guess_int = input('Enter a guess between 0 - 10: ')
    # Convert the user's number to integer (as long as input() returns string)
    guess = int(guess_int)

    # Generate random number using randint 
    randomi = randint(0,10)
    # Check if user's guess equal to computer's number
    if guess == randomi:
        # Print to user that the guess is right
        print ('Right!')
        print (randomi)
    
    # Check if user's guess is morte than computer's number
    elif  guess > randomi:
        # Print to user that it is more
        print ('Too high! The number was',randomi,'! :p')


    # If it's not equal or more
    else:
        print ('Too low! The number was',randomi,'! :p')
        # Print that it's too small
