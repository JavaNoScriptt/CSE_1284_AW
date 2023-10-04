# life_test_program_3
#
# This program tests the countLiveNeighbors function.
#
# You may modify this test program. This file will NOT be graded.
# Only the code in life_module.py gets graded.



# you must import the life module to test countLiveNeighbors
import life_module




# create a small test grid
#
#     01234 columns
# rows
#  0  00000
#  1  01100
#  2  01100
#  3  00000
#
# these are the live neighbor counts you should get for each cell
#
#     01234 columns
# rows
#  0  12210
#  1  23320
#  2  23320
#  3  12210

testGrid = [[0,0,0,0,0],
            [0,1,1,0,0],
            [0,1,1,0,0],
            [0,0,0,0,0]]


# count the live neighbors for a cell at some row and column

row = 1
col = 2

neighborCount = life_module.countLiveNeighbors( testGrid, row, col )

print( "cell at row", row, "and col", col, "has", neighborCount, "live neighbors" )



# The test above is very simple.
# Try iterating over all the cells of the test grid
# and pretty printing a grid of neighbor counts.


# Counting neighbors for cells at the edges and corners can be tricky.
# It is easier if you think of "tiling" the grid.
# Remember that the left and right edges touch
# and the top and bottom grid edges touch too.
#
# A grid like this has live cells at the corners.
#
# 1000
# 0000
# 0001
#
# If you draw the grid tiled, you will see those corners are neighbors.
#
# 1000|1000|1000
# 0000|0000|0000
# 0001|0001|0001
# ----+----+----        For each cell, we look at 8 neighbor cells N
# 1000|1000|1000        but we don't look at the central cell C
# 0000|0000|0000
# 0001|0001|0001                        NNN
# ----+----+----                        NCN
# 1000|1000|1000                        NNN
# 0000|0000|0000
# 0001|0001|0001
#
# Therefore, the live neighbor counts for this grid look like this:
#
# 1112
# 2112
# 2111
#
# Try writing test code with the grid from this example.
   


