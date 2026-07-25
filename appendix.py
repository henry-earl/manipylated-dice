import Dice.repo.manipylated_dice as manipylated_dice
import pandas as pd
import numpy as np

###
# A test designed to show how for an arbitrarily large dice, if you have a larger standDev variable the data from our approximation gets more accurate.
# We show this by increasing the standDev variable of our dice object and rolling it 10,000 times with each.
# We then check to see how much data falls with in 1, 2 and 3 standard deviations.
# We hoped our test would show an increase in accuracy the larger our standDev variable.
# It does.
###

#Sets Seed for reproducable results
np.random.seed(999)


#Table for data
columns = ["=5", "=10", "=15"]
rows = ["1 Standard Deviation (68%)", "2 Standard Deviation (95%)", "3 Standard Deviation (99.7%)"]
data = []



# Dice parameters
sides = tuple(i for i in range(1000))
changing_standDev = [5, 10, 15]
mean = 500



# Loop changing the standDev variable of the dice
for i in changing_standDev:
    test_dice = manipylated_dice.normalDice(sideNames=sides, mean = mean, standDev = i)

    # tuple holding the data of 10,000 rolls of the dice
    tempdata = manipylated_dice.roll(test_dice, noRolls=10000)
    tempdata_input = []

    # Loop for checking with in 1,2,3 standard deviations in turn
    for x in range(1, 4):
        # resets the count variable when checking next stand deviation
        count = 0

        # loops through tempdata
        for y in tempdata:
            # check each item "y" if it is with in each bound of the standard deviation currently being checked. x = (1, 2, ,3), i = (5, 10, 15)
            if y <= (mean + x*i) and y >= (mean - x*i):
                count += 1

# Inputs data into the data frame
        tempdata_input.append(f"{count/100}%")
    data.append(tempdata_input)
df = pd.DataFrame(data, columns, rows)
print(pd.concat([pd.concat([df],keys=['Results with in:'], axis=1)],keys=['StandDev']))