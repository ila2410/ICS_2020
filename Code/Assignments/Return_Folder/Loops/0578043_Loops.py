
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
while len(students) != 0:
    # if length of the list is mod of 2 (% operator)
    if len(students)%2 == 0:
        # our group will be group A
        group = 'Group A'

    # else
    else:
        # group B
        group = 'Group B'

    # Now it is time to choose a student
    # Choose a student using choice() function
    student = choice(students)

    # Add chosen student to the group in the dictionary
    groups[group].append(student)

    # Remove student from the list
    students.remove(student)


# Outside the loop print() your groups
print(groups)