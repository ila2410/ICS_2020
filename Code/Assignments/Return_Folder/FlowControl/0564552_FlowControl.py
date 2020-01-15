
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

    # Print welcoming words
    print("Hey, welcome to da game!")

    # Generate random number using randint 
    random_number = randint(0,101)

    while(True):

        # Get a number from user by input() function
        user_num = input("Pick a number from 0 to 100! ")

        try:
            # Convert the input from user to int
            user_number_int = int(user_num)

            # Check if user's guess equal to computer's number
            if user_number_int == random_number:
                # Print to user that the guess is right
                print("Your guess is correct!\n")
                break
    
            # Check if user's guess is morte than computer's number
            elif user_number_int > random_number:
    
                # Print to user that it is more
                print("Sigh, it's too big!")

            # If it's not equal or more
            else:
                # Print that it's too small
                print("Too small :D")

        except:
            print("Input is not a number. Try again!")
