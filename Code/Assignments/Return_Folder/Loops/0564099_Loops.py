import random
from random import choice

students = ["Andy", "Michael", "Jane", "Jacob", "Stan", "Andrew", "Max"]
groups = {"Group A" : [], "Group B" : []}

while (len(students) != 0):
    the_student = choice(students)
    if (len(students) % 2) == 0:
        groups["Group A"].append(the_student)
        students.remove(the_student)
    else:
        groups["Group B"].append(the_student)
        students.remove(the_student)
else: 
    print("The group division has been done!") 
    print()
    print("Here is group A: " + str(groups["Group A"]))
    print("Here is group B: " + str(groups["Group B"]))