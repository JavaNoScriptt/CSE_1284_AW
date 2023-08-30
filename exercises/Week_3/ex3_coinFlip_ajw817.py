#Coin Flip with ifs
from random import randint
#imports a random function from python

#Gets a random number that is 0 or 1
#Credit to my highschool teacher for teaching me this exact formula to get a more truly random number

flip = (randint(0,10)+1)%2

#Basic if else statements
if flip == 1:
    print('Heads')
else:
    print('Tails')