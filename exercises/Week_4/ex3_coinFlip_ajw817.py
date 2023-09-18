#Coin flip without if/else or string concationation
#Uses list/tuples

#this makes things more simple because you do not have too do random.randint() just randint()
from random import randint


#This could be either a list or a tuple beause you are not adding or changing any of the items in the list/tuple
coin_sides  =['Heads', 'Tails']

flip = (randint(0,10)+1)%2 #Either 0 or 1 can come out of this function

#Prints either heads or tails
print(coin_sides[flip])