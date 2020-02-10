import time

duration = ""

while (type(duration) != int): 
    try:
        duration = int(input("Please, give duration for the timer:\n\n"))
    except:
        print("The input you gave is not a number. Please, change your input.\n")
        time.sleep(2)

start_time = time.time()
current_time = 0
print()

while (current_time < duration):
    current_time = (time.time() - start_time)
    time_left = int(duration - current_time)
    print(time_left, end="\r")
else:
    print("\n\nThank you!")