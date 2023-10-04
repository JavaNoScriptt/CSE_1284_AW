# life_test_program_1
#
# This program tests the gridToString function.
#
# You may modify this test program. This file will NOT be graded.
# Only the code in life_module.py gets graded.



# You need to import life_module to use the gridToString function

import life_module


# create a grid of 1's and 0's to convert to a string
# start with small tests!
#
# should convert to this string
#
# OOO
# +++
# ++O

lifeGrid = [[1,1,1],
            [0,0,0],
            [0,0,1]]


# convert the grid to a string
gridStr = life_module.gridToString( lifeGrid )

# print the string!
print( gridStr )
print('')


# a larger test grid
lifeGrid = [ [0,0,0,0,0,0,0],
             [0,1,1,0,0,0,0],
             [0,1,1,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,1,1,1],
             [0,0,0,0,0,0,0] ]


# convert the grid to a string
gridStr = life_module.gridToString( lifeGrid )


# print the string!
print( gridStr )
print('')






