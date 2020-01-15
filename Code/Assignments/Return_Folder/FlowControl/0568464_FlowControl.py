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

from random import randint 

print('Hello username!')
print('Guess a number from 0-10: ')
user_input = int(input())
random_number = randint(0,11)

if user_input == random_number:
    print('Your guess is right!')

elif user_input > random_number:
    print('Your number is greater.')

elif user_input < random_number:
    print('Your number is too small.')