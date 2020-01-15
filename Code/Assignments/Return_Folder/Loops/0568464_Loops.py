
# Today's assignment is about 
# Splitting students two into groups
# 
#=================================#
#            Ingredients          #
#---------------------------------#
#     from random import choice   #
#           list.remove()         #
#               list()            #
#               len()             #
#                %                #
#=================================#
from random import choice

# Here is your list of students
# Your goal is to randomly split them into groups
students = ['Andy', 'Michael', 'Jane', 'Jacob', 'Stan', 'Andrew', 'Max']

# Create dictionary with groups 
groups = {'Group A' : [], 'Group B' : []}

# Use while loop to split students
# Iterate till there are no students in the list
#  You can check amount of students by len() function 

# if length of the list is mod of 2 (% operator)
# our group will be group A

while len(students) > 0:

	if len(students) % 2 == 0:
		group = 'Group A'
		student = choice(students) # Now it is time to choose a student. Choose a student using choice() function
		students.remove(student) # Remove student from the list
		groups[group].append(student) # Add chosen student to the group in the dictionary
	    
		
	elif len(students) % 2 == 1:
		group = 'Group B'
		student = choice(students) # Now it is time to choose a student. Choose a student using choice() function
		students.remove(student) # Remove student from the list
		groups[group].append(student)  # Add chosen student to the group in the dictionary
	
else:
	print(groups) # Outside the loop print() your groups

