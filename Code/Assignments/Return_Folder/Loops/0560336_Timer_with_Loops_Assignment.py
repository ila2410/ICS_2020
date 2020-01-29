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
import time

# time.time() returns elapsed time since from year 1970
# Store start time using time.time()


# Initiate a value with duration of the timer
# This variable will be used with input() function, therefore, it should be a string
# Now initiate an empty string
duration = ''

# Use while loop to ask user duration of the timer
# While type of duration will not change to integer, loop and ask user to input value again
# The condition in that sense will be following:
# type(variable) != int
# Put condition to while loop

while type(duration) != int:

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

        duration = int(input('Please set a timer:'))

    except:

        # This part of code will be executed when Python throw an exeption
        # Print here, that user didn't type correct input
        print('That is not the correct input!')

        # Outside of the previous loop initiate a variable where you will store start time
        # You can get time by using time.time() function. Note, that it shows time in seconds from year 1970.
        # For more info follow the link:
        # https://docs.python.org/3/library/time.html
start_time = time.time()

# Now initiate variable where you will store current time at the each iteration of the loop
# For now it can be 0
current_time = 0


# Use while loop for iterating while current_time value less than duration
# You can compare variables with < operator(less operator)
while current_time < duration:

    # Get current time value. You can do it by assigning value of (time.time() - start_time)
    current_time = (time.time() - start_time)

    # Calculate how much time left till the end of the timer.
    # You can do it by difference of duration and current time
    time_left = duration - current_time

    # Print time_ left value. You can do it even fancier.
    # You can print it on one line. You can do it as follows:
    # print(variable, end="\r")
    print(time_left, end='\r')


# If you want, you can do a stopwatch down here. But it is optional.
# def means define a function, everytime the function name is called, the function will be executed
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), int(sec)))
# end of function


# now  code for the user
input("Press Enter to start")
# start_time will get a new value, because the old start_time started when the programm was started
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time

time_convert(time_lapsed)
