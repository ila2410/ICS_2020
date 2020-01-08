
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
    print('Hello!')

    # Get a number from user by input() function
    user_number = input('your randing from 0 to 10,')

    # Convert the user's number to integer (as long as input() returns string)
    user_number_int = int(user_number)

    # Generate random number using randint 
    random_num = randint(0,10)
    # Check if user's guess equal to computer's number
    if user_number_int == random_num:
        # Print to user that the guess is right
        print('Concrats! Correct number!')
    
    # Check if user's guess is morte than computer's number
    elif user_number_int > random_num:
    
        # Print to user that it is more
        print('Number is too big!')

    # If it's not equal or more
    else:
        # Print that it's too small
        print('Number is too small')