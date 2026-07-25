# Simulating Dice with Python 

Henry Earl, Krishna Kumar, Morgan Stoddart, Jonathan Willis April 2025 

### **Abstract** 

This paper introduces Manipylated Dice: a Python library that allows for the creation and rolling of various dice. These dice are either rolled with set probabilities or such that the result is approximately normally distributed. 

The functionality of the library and the rolling of a die which after a arbitrarily large number of rolls will have results that form an approximate normal distribution will be described. 

## **1 Introduction** 

Dice have been a key component of many different games in many different cultures for thousands of years and are still used in about a quarter of board games played today, with 41738 of the 163804 board games on BoardGameGeek being tagged as including a die-rolling mechanic at the time of publication. 

Dice are made out of a few essential elements: 

1. A set number of sides. 

2. A corresponding arbitrary value for each side. 

3. A probability or weighting that is given to each side that totals to one when all sides are combined. 

The Manipylated Dice library aims to allow the creation of dice following the above parameters and the simulation of the rolling of these dice n-times. Dice can be created with either set probabilities or following an approximate normal distribution. 

In addition to the simple creation and rolling of various created dice the library also enables the rolling of multiple dice at once. There is also a separate function that increases the probability of rolling a double compared to the original given probability of the die. 


## **2 Rolling an Approximate Normal Distribution** 

The Manipylated Dice library can be used to generate a dice that rolls in an approximate normal distribution. 

However, as the normal distribution is continuous but the results of a dice roll with a set number of sides is discrete; the rounding of the continuous results of the normal distribution to the discrete results of the rolling of a die creates an over-concentration of results being mapped to values close to the mean especially at smaller standard deviations. 

This increasing accuracy of the approximation of the normal can be seen in Table 1 below which was obtained by rolling a die with 1000 sides, 10,000 times with a mean, _µ_ = 500 and changing the StandDev variable: 

|StandDev|Results within: _σ_ (68%)|2_σ_ (95%)|3_σ_ (99.7%)|
|---|---|---|---|
|5|72.69%|96.19%|99.84%|
|10|71.43%|96.08%|99.75%|
|15|69.84%|95.49%|99.74%|



Table 1: Table showing the change in accuracy of the approximate normal distribution for increasing StandDev variable. 

This shows that for a more accurate approximation of the normal distribution a higher standard deviation should be used. 

## **3 Conclusion** 

This paper has given a description of Manipylated Dice: a library which allows the creation and rolling of different dice. 

Due to the library being object oriented it’s features can be easily utilised and manipulated by a user to create more complex tools. 

Also, the library is written in a fully modular way, is well documented and is automatically tested. 