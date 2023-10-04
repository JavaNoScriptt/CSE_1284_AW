# life_test_program_4
#
# This program tests the gridUpdate function.
#
# You may modify this test program. This file will NOT be graded.
# Only the code in life_module.py gets graded.



# you must import the life module to test gridUpdate
import life_module


# IMPORTANT!!!
#
# gridUpdate needs to call countLiveNeighbors so make sure it works
# before trying to implement or test gridUpdate
#
# You should also have gridToString working so you can pretty print
# your grids when you test your functions.
#
# Finally, if you want to perform multiple gridUpdate calls,
# you must swap the grids between calls to gridUpdate.
# Thus gridSwap better be working.


# Here is a simple test to start with.
# The blinker switches from horizontal to vertical and back again each turn.
# Start with a horizontal blinker. After one grid update, you should have
# a vertical blinker.

# horizontal blinker in the previous grid
life_module.gridPrevious = [[0,0,0,0,0],
                            [0,0,0,0,0],
                            [0,1,1,1,0],
                            [0,0,0,0,0],
                            [0,0,0,0,0]]

# put just zeros in the current grid for now
life_module.gridCurrent = [[0,0,0,0,0],
                           [0,0,0,0,0],
                           [0,0,0,0,0],
                           [0,0,0,0,0],
                           [0,0,0,0,0]]

# do a grid update
life_module.gridUpdate()

# there should now be a vertical blinker in the current grid

print( "previous grid\n" )
print( life_module.gridToString( life_module.gridPrevious ), '\n' )

print( "current grid\n" )
print( life_module.gridToString( life_module.gridCurrent ), '\n' )


# Now do a grid swap.
# The current grid becomes the previous grid
# and the old previous grid can now be used as the current grid.
# The vertical blinker should be in the previous grid (print grids to check)

# TODO - you write the code to test this


# Now do another grid update.
# If you want to be really sure gridUpdate is working,
# you could set the current grid to all zeros again before doing the update.

# TODO - you write the code to test this


# now print your grids
# There should now be a horizontal blinker in the current grid again.

# TODO - you write the code to test this

