import math
import random
import string

# ask user how long password should be
# ask if numbers
# ask if lowercase letters
# ask if upercase letters
# ask if special character
# check if 'y' or 'n' was typed otherwise notify user

length = input('How long should the password be? \t')
num = input('Do you need numbers? y/n \t')
lette = input('Do you need letters? y/n \t')
spch = input('Do you need special characters? y/n \t')

# change password length into a integer because its easier to go on with  this
pwlen = int(length)

# generate random numbers and letters in fuctions
"""
sample.choice() prevents repeating numbers or letters to
be there twice normaly it would be random.choice()
ascii is for letters in Asci code

to pick a single character from a string constant using
a random.choice()/random.sample() function and add it to the string 
ariable using a join function. The choice/sample function
used to choose a single character from a list.
"""

# generate random Numbers
# random.choice was used because there would be an error when the PW gets longer then 10


def Number(pwlen):
    numbers = string.digits
    return ''.join(random.choice(numbers)for i in range(pwlen))


#print('The random number is:', Number(pwlen))


# generate random letters
def Letters(pwlen):
    lett = string.ascii_letters
    return ''.join(random.sample(lett, pwlen))


#print('The random letters is:', Letters(pwlen))


# generate random special characters
def Special(pwlen):
    spcharacters = string.punctuation
    return ''.join(random.sample(spcharacters, pwlen))


#print('Special Characters are:', Special(pwlen))

# __________________________________________________________________________________________

# function radom numbers and letters


def NumLetter(pwlen):
    numlett = string.digits + string.ascii_letters
    return ''.join(random.sample(numlett, pwlen))


#print('Numbers and Letters:', NumLetter(pwlen))


# function numbers and special characters
def NumberSpecial(pwlen):
    numspecial = string.digits + string.punctuation
    return ''.join(random.sample(numspecial, pwlen))


#print('Numbers and special characters:', NumberSpecial(pwlen))

# funtion Letters and Special characters


def LetterSpecial(pwlen):
    letterspe = string.ascii_letters + string.punctuation
    return ''.join(random.sample(letterspe, pwlen))


#print('Letter and Special Characters:', LetterSpecial(pwlen))

# function Numbers, Letters and Special characters


def All(pwlen):
    allcases = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(allcases, pwlen))


#print('All is:', All(pwlen))


# generate statement
if num != 'y' and lette != 'y' and spch != 'y':
    print('You didnt choose something!')
elif num == 'y' and lette != 'y' and spch != 'y':
    print('Password with Numbers:', Number(pwlen))
elif num != 'y' and lette == 'y' and spch != 'y':
    print('Password with letters:', Letters(pwlen))
elif num != 'y' and lette != 'y' and spch == 'y':
    print('Password with Special Characters:', Special(pwlen))
elif num == 'y' and lette == 'y' and spch != 'y':
    print('Password with Numbers and Letters:', NumLetter(pwlen))
elif num == 'y' and lette != 'y' and spch == 'y':
    print('Password with Numbers and Special Characters:', NumberSpecial(pwlen))
elif num != 'y' and lette == 'y' and spch == 'y':
    print('Password with Letters and Special Characters:', LetterSpecial(pwlen))
else:
    print('Password with Numbers, Letters and Special Characters:', All(pwlen))
