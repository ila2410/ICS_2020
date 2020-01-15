
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
    print('Welcome to guess the number!')

    # Get a number from user by input() function
    user_num = input('Please type in an integer number between 0 and 10: ')

    # Convert the user's number to integer (as long as input() returns string)
    user_to_int = int(user_num)

    # Generate random number using randint 
    com_num = randint(0,10)

    # Check if user's guess equal to computer's number
        # Print to user that the guess is right
    # Check if user's guess is more than computer's number
        # Print to user that it is more
    # If it's not equal or more
        # Print that it's too small
    if user_to_int == com_num:
        print('You guessed right!')
    elif user_to_int > com_num:
        print('Your guess is bigger!')
    else:
        print('Your guess is smaller!')
        

    
    


    
