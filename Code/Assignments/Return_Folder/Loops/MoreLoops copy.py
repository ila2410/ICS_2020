import os

# List of Fibonacci numbers
fibonacci_sequence = [0,1,1,2,3,5,8,13,21,34,55]

# We can make a fibonacci sequence by ourselves
our_fibonacci_sequence = []
amount_numbers = 15
first_number = 0
second_number = 1

for number in range(amount_numbers):
    print(first_number)
    our_fibonacci_sequence.append(first_number)
    new_fibconacci_number = first_number + second_number

    first_number = second_number
    second_number  = new_fibconacci_number

# Open files in the folder 
#path = '/some/path/to/file'
path = 'C:/Data/TextFiles'
#try:
for filename in os.listdir(path):
    file_path = '{}/{}'.format(path,filename)
    text_file = open(file_path, 'r')
    line = text_file.readline()
    print(line)
#except:
    #print('No such directory! Check if you wrote it correctly!')
