
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
number_of_students = len(students)

while number_of_students > 1:
    number_of_students = len(students)

    # if length of the list is mod of 2 (% operator)
    if(number_of_students % 2 == 0):
        # our group will be group A
        the_output_group = groups['Group A']

    # else 
    else:
        # group B
        the_output_group = groups['Group B']

    # Now it is time to choose a student
    # Choose a student using choice() function
    selected_student = choice(students)
    print(number_of_students, selected_student)


    # Add chosen student to the group in the dictionary
    the_output_group.append(selected_student)

    # Remove student from the list  
    students.remove(selected_student)

# Outside the loop print() your groups

# Print each student from the original list on the same line with an empty space in between

print("")
print("Group A")

# For each student in group A
for student in groups['Group A']:

    # Print each student on the same line with an empty space in between
    print(student,end=" ")

# Print extra lines
print("")
print("")

print("Group B")

# For each student in group B
for student in groups['Group B']:

    # Print each student on the same line with an empty space in between
    print(student,end=" ")

