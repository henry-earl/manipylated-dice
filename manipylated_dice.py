import random
import numpy as np
import matplotlib.pyplot as plt

def roll(arg, noRolls = 1):
    """
    Makes a selction on type of roll based on a dice objects "type" attribute

     - CUSTOM ROLL
        Rolls a given ammount of times a custom dice object (dice with set sides and set side probabilities)
        Returns these rolls as a tuple.

     - NORMAL ROLL
        Randomly generate discrete values to fit a normal distibution.
        Done by generating numbers in a normal distribution, rounding them and then checking if they are with in bounds before adding them to a list
        Generated results not within bounds are ignored and regenerated. (This skews accuracy and this is discussed in our paper)
        As inputted sides might not be linear a temporary list of linear numbers is created.
        Then inputted sides can be treated as if they are linear (we assume they are inputted in ascending order)
        A temporary mean is then taken from this new list based on its position in original sideNames list.
        Once results are generated, we converted back before returning a tuple.

    Parameters
    ----------
    arg
        A dice object.
    noROlls
        An int variable defaulted to 1 that dictates how many times dice is rolled.

    Returns
    -------
    tuple
        The outcomes of the dice roll.
    """
    if arg.type == "custom":
        return tuple(np.random.choice((arg.sideNames), noRolls, p=arg.sideProbs))

    elif arg.type == "normal":
        tempSideNames = [i for i in range(len(arg.sideNames))]
        tempMean = tempSideNames[arg.sideNames.index(arg.mean)]
        templist = []

        while len(templist) < noRolls:
            temp = round(np.random.normal(tempMean, arg.standDev))

            if temp >= 0 and temp <= len(tempSideNames)-1:
                templist.append(temp)
              
        return tuple(arg.sideNames[tempSideNames.index(item)] for item in templist)
    
    return ("Invalid dice type")



def multiRoll(*args, noRolls = 1):
    """
    Input as many dice objects as required and how many rolls
    Useful for dice games with multiple types of dice.

    Parameters
    ----------
    *args
        An unkown number of dice objects.
    noROlls
        An int variable defaulted to 1 that dictates how many times each dice object is rolled.

    Returns
    -------
    tuple
        Contains tuples of the outcomes of each dice rolls.
    """
    output = []

    for i in range(len(args)):
        output.append(roll(args[i], noRolls))

    return tuple(output)



def doubleRoll(arg, doubleProb):
    """
    Returns a double roll a given probability of times
    The output that is doubled is from a standard roll
    Otherwise it returns two independant rolls.

    Parameters
    ----------
    arg
        A dice object.
    doubleProb
        A float variable that determines the chance a roll is double.

    Returns
    -------
    tuple
        A tuple containing two tuples with the outcomes of the two rolled dice.
    """
    if random.random() > doubleProb:
        temp = roll(arg, 2)
        return tuple(tuple(temp[0]), tuple(temp[1]))
        
    else:
        temp = roll(arg)
        return (temp[0], temp[0])
        




class dice():
    """
    Class for Dice Objects
    """
    def __init__ (self, sideNames):
        self.sideNames = sideNames
      
class customDice(dice):
    """
    Subclass of 'dice' for Dice Objects with Custom side probabilitys.
    """
    def __init__(self, sideProbs, sideNames):
        #Run Parent class init
        super().__init__(sideNames)
        self.type = "custom"
        self.sideProbs = sideProbs

class normalDice(dice):
    """
    Subclass of 'dice' for Dice Objects with Normal Distributions.
    """
    def __init__(self, sideNames, mean, standDev):
        #Run Parent class init
        super().__init__(sideNames)
        self.type = "normal"
        self.mean = mean
        self.standDev = standDev



#Some premade objects
d6 = customDice(sideNames=[1,2,3,4,5,6],
                sideProbs=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

d10 = customDice(sideNames=[0,1,2,3,4,5,6,7,8,9],
                 sideProbs=[1/10,1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10])

d20 = customDice(sideNames=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                 sideProbs=[1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20, 1/20])