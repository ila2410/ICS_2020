
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

if __name__ == "__main__":

    # Print welcomming words
    
    print("Hello! Let's play guess a number game!")

    # Get a number from user by input() function
    
    number_str = input('What is your number (from 0 to 10)? \n')
    
    # Convert the user's number to integer (as long as input() returns string)
    
    number = int(number_str)

    # Generate random number using randint 
    
    random_number = randint(0,10)

    # Check if user's guess equal to computer's number
    
    if (number == random_number):

        # Print to user that the guess is right
        
        print('You guess the right number, congratulations!!')
    
    # Check if user's guess is more than computer's number
    
    elif (number > random_number):

        # Print to user that it is more
        
        print('Your number is higher than the computer number!')

    # If it's not equal or more
    
    else:

        # Print that it's too small
        
        print('Your number is too small, try again!')
