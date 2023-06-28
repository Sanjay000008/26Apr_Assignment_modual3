# How can you get a random number in python? 

""" In Python We should import random and use random.randint()function is defined in random modual.

"""
import random

y="y"
while y!="n":
    t=random.randint(11111,99999)
    print(t)
    y=input("Do you wan't to countinue 'y' for 'yes' 'n' for 'no' :-")
    