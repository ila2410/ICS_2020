
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
    print('Let\'s play a game of guess a number!')

    # Get a number from user by input() function
    user_number_str = input('Please type in a number from 0 to 10! ')

    # Convert the user's number to integer (as long as input() returns string)
    user_number_int = int(user_number_str)

    # Generate random number using randint 
    random_num = randint(0, 10)

    # Check if user's guess equal to computer's number
    if user_number_int == random_num:
        # Print to user that the guess is right
        print('The number {} is correct!'.format(random_num))
    
    # Check if user's guess is more than computer's number
    elif user_number_int > random_num:
            
        # Print to user that it is more
        print('The number {} is too large. The correct number is {}.'.format(user_number_int, random_num))

    # If it's not equal or more
    else:
     
        # Print that it's too small
        print('The number {} is too small. The correct number is {}.'.format(user_number_int, random_num))
