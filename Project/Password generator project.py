import random,sys
words = [
"Interference","Coal","Endure","Deck","Waiter","Empirical","Mushroom","Example","Arrangement","Thumb","Bubble","Mosquito","Vacuum","Ritual","Book","Battle","Laborer","Suite","Accumulation","Listen","Comprehensive","Flush","Resource","Appointment","Funny","Romantic","Wine","Plagiarize","Final","Right","Wing","Length","Kill","Stool","East","Determine","Crack","Cast","Accumulation","Forestry","Nose","Rotation","Convict","Can","Opponent","Steep","Finger","Commemorate","Teenager","Greet","Ghostwriter","Feedback","Demonstration","Drill","Length","Professional","Outer","Wine","Summary","Purpose","Virgin","Housing","Duck","Researcher","Copper","Layer","Eye","Compose","Network","Feminine","Traffic","Patrol","Habit","Register","Confusion","Execute","Slip","Clerk","Contact","Part","Low","Violation","Head","Contradiction","Creation","Asset","Prevalence","Recession","Trouble","Assembly","Marsh","Selection","Trick","Bond","Restless","Steward","Prestige","Aluminium","Follow","Projection","Project","Policy","Evoke","Sink","Hell","Spell","Poll","Pie","Award","Hard","Devote","Reform","Owl","Intention","Mine","Cope","Crouch","Graphic","Disaster","Cousin","Document","Ideology","Fossil","Resource","Eagle","Adjust","Pole","Pop","Coup","Faithful","Finish","Variety","Church","Predator","Climb","Action","Training","Clearance","Hospitality","Welcome","System","Taste","Remark","Left","Mistreat","Tire","Steam","Integrity","Build","Offspring","Agile","Affinity","Nightmare","Crop","Autonomy","Whip","Account","Lover","Wound","Rate","Volcano"]

def changeCharacter(inChr):
    outChr=""
    # Changinng the following characters : a,i,o,e,z 
    if inChr == "a":
        outChr = "@"
    elif inChr == "i":
        outChr = "!"
    elif inChr == "o":
        outChr="0"
    elif inChr=="e":
        outChr="3"
    elif inChr=="z":
        outChr="7"
    # If the character is not one of those the output will be the same as the input 
    else:
        outChr=inChr
    # Only with a 50% chance the character will change 
    chance = random.randint(1,100)
    if chance <= 50:
        return outChr
    else: 
        return inChr

# Main function
if __name__== "__main__":
    # This is the password, initially empty     
    password = ""

    # Greeting message
    print("Hello. I will generate you a random password from a list of " +  str(len(words)) + " words.")

    # Get info from user
    while True:
        try:
            number_of_words = int(input("How many words? "))
            number_of_digits = int(input("How many digits? "))
            break
        #if the above fails the following will happen
        except:
            print("please enter a number")   

    # The loop picks a random word from the list of words
    # Password = password+random_word concatenates the strings together 
    for i in range(number_of_words):
   
        random_word = random.choice(words)
        password=password+random_word

    # The loop picks user determined number of digits, and combines them together with the random words and creates the password
    for i in range(number_of_digits):

        w = random.randint(0,9)
        password=password+str(w)

    new_password=""

    # The loop goes through each character and changes them according to the function
    for i in range(len(password)):
        character= password[i]
        newCharacter= changeCharacter(character)
        new_password=new_password+newCharacter
        
    # Print passwords 
    print("")
    print("Here is your strong password: " + new_password)
    print("Here is your weak password: " + password)

  


