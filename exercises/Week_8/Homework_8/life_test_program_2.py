# life_test_program_2
#
# This program tests the gridSwap function.
#
# You may modify this test program. This file will NOT be graded.
# Only the code in life_module.py gets graded.


# import the life module so you can test gridSwap
import life_module



# give the current grid and previous grid some values
life_module.gridPrevious = [ [1,1,1], [0,0,0] ]
life_module.gridCurrent  = [ [1,0,0], [0,1,1] ]

# grid IDs before swap
idCurrent  = id(life_module.gridCurrent)
idPrevious = id(life_module.gridPrevious)

print( "grid id and value before swap" )
print( "gridCurrent: ", idCurrent,  life_module.gridCurrent )
print( "gridPrevious:", idPrevious, life_module.gridPrevious )

# swap the previous and current grids
life_module.gridSwap()

# grid IDs after swap
idCurrent2  = id(life_module.gridCurrent)
idPrevious2 = id(life_module.gridPrevious)

print( "\ngrid id and value after swap" )
print( "gridCurrent: ", idCurrent2,  life_module.gridCurrent )
print( "gridPrevious:", idPrevious2, life_module.gridPrevious, '\n' )


    

