# Today's assignment is about 
# Splitting students two into groups
# 
#=================================#
#            Ingredients          #
#---------------------------------#
#            import time          #
#            time.time()          #
#              input()            #
#               int()             #
#            try-except           #
#                 <               #
#=================================# 



# Import time module


# time.time() returns elapsed time since from year 1970
# Store start time using time.time() 


# Initiate a value with duration of the timer
# This variable will be used with input() function, therefore, it should be a string
# Now initiate an empty string
duration = ______

# Use while loop to ask user duration of the timer
# While type of duration will not change to integer, loop and ask user to input value again
# The condition in that sense will be following:
# type(variable) != int
# Put condition to while loop

while ______:

    # We will skip learning of try/except block,
    # but long story short, it allows to continue to execute code
    # even if there is an error.
    # In our case, if user's input is not a number and we will try to
    # convert it to integer, then Python will throw an error.
    # You can read about try-except block from here: https://wiki.python.org/moin/HandlingExceptions
    
    try:
        # Ask for input value using input() function. Try-except needs indentation.
        # Then convert it at the same place to the integer as follows:
        # variable = int(input('Whatever you want to write to user\n')).
        # By the way, \n at the end of the string means that user will
        # type his number to the next line in the console.
        # Try to experiment with that.

        duration = ________
    
    except:

        # This part of code will be executed when Python throw an exeption
        # Print here, that user didn't type correct input
        

# Outside of the previous loop initiate a variable where you will store start time
# You can get time by using time.time() function. Note, that it shows time in seconds from year 1970.
# For more info follow the link:
# https://docs.python.org/3/library/time.html
start_time = _________

# Now initiate variable where you will store current time at the each iteration of the loop
# For now it can be 0 
current_time = 0


# Use while loop for iterating while current_time value less than duration 
# You can compare variables with < operator(less operator) 
while _________:

    # Get current time value. You can do it by assigning value of (time.time() - start_time)
    current_time = _________

    # Calculate how much time left till the end of the timer.
    # You can do it by difference of duration and current time
    time_left = ________

    # Print time_ left value. You can do it even fancier.
    # You can print it on one line. You can do it as follows:
    # print(variable, end="\r") 



# If you want, you can do a stopwatch down here. But it is optional.

