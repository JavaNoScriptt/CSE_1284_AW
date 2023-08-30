#Coin Flip without ifs
from random import randint
#imports a random function from python

#Gets a random number that is 0 or 1
#Credit to my highschool teacher for teaching me this exact formula to get a more truly random number

flip = (randint(0,10)+1)%2

#The math here is made in such a way that one variable is zero but the other one is a one
mult_heads = 0 + flip
mult_tails = 1 - flip

#
print( mult_heads * "Heads" + mult_tails * 'Tails')  