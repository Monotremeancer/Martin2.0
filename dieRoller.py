import re
import random

def dieRoll(roll):
    expression = r"(\d*)([dD][sS]*)(\d+)([+-]*)(\d*)"
    rollstring = re.match(expression, roll)

    #### Determines what to roll ####
    toRoll = []
    positions = [1,3,5] # Number, type if die, modification
    for i in positions:
        try:
            toRoll.append(int(rollstring[i])) # Check the value
        except:
            toRoll.append(0) # If a value is not given, assume 0


    #### If it is just a normal die ####
    if rollstring[2].lower() == "d":
        rolls = [random.randint(1, toRoll[1]) for _ in range(0, toRoll[0])]  # Roll the correct die

        rollSum = sum(rolls)

        if rollstring[4] == "+": # Add a potential modifier
            roll = rollSum + toRoll[2]

        elif rollstring[4] == "-": # Subtract a potential modifier
            roll = rollSum - toRoll[2]

            if roll < 1: #If it subtracts to less than 1, make it a 1
                roll = 1

        return(rolls, roll) #Return the rolls and the total sum



    else:
        return("Rulle en D-vadå?")

print(dieRoll("7d10+1"))