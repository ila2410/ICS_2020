
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
while len(students) > 0:
    if len(students) % 2:
        
        group = 'Group A'
    else:
        group = 'Group B' 

    # Iterate till there are no students in the list
    #  You can check amount of students by len() function 


    # if length of the list is mod of 2 (% operator)
        # our group will be group A

    # else 
        # group B

    # Now it is time to choose a student
    # Choose a student using choice() function
    the_chosen_one=choice(students)
    groups[group].append(the_chosen_one)
    # Add chosen student to the group in the dictionary

    # Remove student from the list   
    students.remove(the_chosen_one)
# Outside the loop print() your groups
print(groups)