
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
    print("Let's play a game!")

    # Generate random number using randint 
    rng = randint(0,11)

    while(True):

        # Get a number from user by input() function
        user_num = input("Write down your number from 0 to 10 \n")

        # Safety check
        try:

            # Convert the user's number to integer (as long as input() returns string)
            user_num_int = int(user_num)


            # Check if user's guess equal to computer's number
            if(user_num_int == rng):

                # Print to user that the guess is right
                print("Correct!\n")
                break

            # Check if user's guess is morte than computer's number
            elif(user_num_int > rng):

                # Print to user that it is more
                print("Too high\n")

            # If it's not equal or more
            else:

                # Print that it's too small
                print("Too small\n")

        # If input is not a number print an error and loop back
        except:
            print("Input is not a number \n")
