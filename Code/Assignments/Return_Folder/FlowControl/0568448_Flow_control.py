
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
    print("enjoy the trick !")

    

    #generating random number for the game
    random_int = random.randint(0,10)
    
    
    
    while(True):
        # Get a number from user by input() function
        user_number = input("pick a number between 0-10\n") 

        #Convert the users number into an integer  
        user_number_integer = int(user_number)
    

        # Check if user's guess equal to computer's number
        if(random_int == user_number_integer):
            print("thats right")
            break

        elif(user_number_integer > random_int):
            print("too high")
        elif(user_number_integer < random_int):
            print("too small")
        
            # Print to user that the guess is right


        # Check if user's guess is morte than computer's number

            # Print to user that it is more


        # If it's not equal or more

            # Print that it's too small