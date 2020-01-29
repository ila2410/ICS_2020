# Aapo Tommila 
# 0553657
#
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
import os
# time.time() returns elapsed time since from year 1970
# Store start time using time.time() 

start_time = time.time()

# Initiate a value with duration of the timer
# This variable will be used with input() function, therefore, it should be a string
# Now initiate an empty string
duration = ''

# Use while loop to ask user duration of the timer
# While type of duration will not change to integer, loop and ask user to input value again
# The condition in that sense will be following:
# type(variable) != int
# Put condition to while loop

print (f'Hello, {os.getlogin()}!')

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

        duration = int(input ('Please give time(s) to run.\n'))
    
    except:
        print ('Your input is not a number!')
        # This part of code will be executed when Python throw an exeption
        # Print here, that user didn't type correct input
        

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
    current_time = time.time() - start_time

    # Calculate how much time left till the end of the timer.
    # You can do it by difference of duration and current time
    time_left = duration - current_time

    # Print time_ left value. You can do it even fancier.
    # You can print it on one line. You can do it as follows:
    # print(variable, end="\r")
    
    print (round(time_left, 2), end='\r')

print ('BOOM!!')
# If you want, you can do a stopwatch down here. But it is optional.


# This has been copied from https://www.geeksforgeeks.org/create-stopwatch-using-python/
# 
import tkinter as Tkinter 
  
counter = -1
running = False
def counter_label(label): 
    def count(): 
        if running: 
            global counter 
  
            # To manage the initial delay. 
            if counter==-1:             
                display="Starting..."
            else: 
                display=str(counter)
  
            label['text']=display   # Or label.config(text=display) 
  
            # label.after(arg1, arg2) delays by  
            # first argument given in milliseconds 
            # and then calls the function given as second argument. 
            # Generally like here we need to call the  
            # function in which it is present repeatedly. 
            # Delays by 1000ms=1 seconds and call count again. 
            label.after(1000, count)  
            counter += 1
  
    # Triggering the start of the counter. 
    count()      
  
# start function of the stopwatch 
def Start(label): 
    global running 
    running=True
    counter_label(label) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
  
# Stop function of the stopwatch 
def Stop(): 
    global running 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
  
# Reset function of the stopwatch 
def Reset(label): 
    global counter 
    counter=-1
  
    # If rest is pressed after pressing stop. 
    if running==False:       
        reset['state']='disabled'
        label['text']='Welcome!'
  
    # If reset is pressed while the stopwatch is running. 
    else:                
        label['text']='Starting...'
  
root = Tkinter.Tk() 
root.title("Stopwatch") 
  
# Fixing the window size. 
root.minsize(width=250, height=70) 
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Arial 30 bold") 
label.pack() 
start = Tkinter.Button(root, text='Startti',  
width=15, command=lambda:Start(label)) 
stop = Tkinter.Button(root, text='Stoppi',  
width=15, state='disabled', command=Stop) 
reset = Tkinter.Button(root, text='Resetti', 
 width=15, state='disabled', command=lambda:Reset(label)) 
start.pack() 
stop.pack() 
reset.pack() 
root.mainloop() 