#!python3
# Explain what this code does

#Imports the random module
import random

#creates a list called x
x = []

#generating 40 random numbers
for i in range(40):

#if number is between 0 to 1
    if random.randint(0,1):

#generate new number between 1 to 10 
#(That will be the number choosen for the list)
        x.append(random.randint(1,10))

#if number is not between 0 to 1
    else:

#generate 2 new number between 1 to 10. Have one divided by 10. Add the 2 new numbers together to get the newest number
#(The newest number will be the number choosen for the list)
        x.append(random.randint(1,10) + random.randint(1,10)/10)

#print the 40 numbers generated
print(x)

#DONE













#Draft

#generating 40 random numbers. If the number is 0 to 1 it generates a new number between 1 to 10
#if the number isn't 0 to 1, 
#then it generates 2 new number between 1 to 10 with one being normal and one divided by 10
#then having them added togther.