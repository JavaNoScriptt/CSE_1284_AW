# life_module.py
#
# data and functions for Conway's Game of Life


# grid for Conway's game of life
#   2D row major list
#   cells contain zero (dead) or non-zero (alive) values
#
# DO NOT CHANGE THESE TWO LINES!
gridPrevious = []
gridCurrent = []

# --------------------------------------------------------------------

# Write the body of the gridToString function.
# The algorithm for the function body has been provided as comments.
#
# A grid like this: [ [0,0,0,0], [0,0,1,0], [1,1,0,0] ]
# Should convert to this string: '++++\n++O+\nOO++\n'
# The string would look like this when printed.
# Return the string. Do NOT print the string in this function!
#
# ++++
# ++O+
# OO++

def gridToString( grid ):
    '''
    Convert a grid used in Conway's Game of Life to its string representation.
    Live cells are represented by the letter O
    Dead cells are represented by the symbol +
    
        Parameters:
            grid (2D integer list, row major)
                The grid stores one integer per cell, either zero (dead cell) or non-zero (live cell)
                
        Returns:
            one string (Str), a representation of the grid
    '''
    
    # YOUR CODE GOES BELOW THIS LINE

    # IMPORTANT!!! Do NOT print anything in this function!
    #              This function does NOT print! It RETURNS a string.
    #              Other code can call this function, get the string,
    #              and print that string. No printing here!
    
    # create an empty string
    bruh = ''
    # for each row in the grid, convert that row
    
        # for each cell in the row, convert the cell
        
            # add symbol to the string for this cell
            #   symbol + for cells that hold a zero
            #   letter O for cells that are non-zero
            
        # add a newline to the string at the end of the grid row
        
    # return the string representation of the grid

# -------------------------------------------------------------------------

# Write the body of the gridSwap function.
#
# The function should swap the current grid (global variable gridCurrent)
# and the grid from the previous step (global variable gridPrevious)
#
# IMPORTANT!  Remember to indicate at the top of your function body
#             what global variables the function needs to alter!
#
# HINT: The pythonic way to swap what two variables refer to is this: a,b = b,a
#
# HINT2: Here's the traditional way to swap if you don't use
#        the more pythonic way
#
#        tmp = a
#        a = b
#        b = tmp

def gridSwap():
    '''
    Swap the current and previous grids.
    
        Parameters: no parameters
        
        Returns: no return value
    '''
    
    # indicate which global variables this function needs to alter
    global gridCurrent
    # TODO - you also need to alter the global variable gridPrevious
    
    # TODO - swap gridCurrent with gridPrevious
    #
    # HINT: Do NOT swap individual cell values! That's inefficient!
    #       Just swap the references to the whole 2D grids.
    
    # this function does not return anything,
    # this return statement just ends the function
    return

# -------------------------------------------------------------------------

# Write the body of the countLiveNeighbors function
#
# HINT: The grid is a row major 2D list of integers.
#       Access an individual cell like this: grid[rowIndex][columnIndex]
#
# HINT2: Live cells have a non-zero value.
#        Dead cells have a zero value.

def countLiveNeighbors( grid, rowIndex, columnIndex ):
    '''
    Returns the number of live neighbors at cell (row,column).

        Parameters
            grid: row major 2D list of integers
            rowIndex: row index of a cell (major index)
            columnIndex: column index of a cell (minor index)
            
            grid[rowIndex][columnIndex] gives a cell value

        Returns:
            neighborCount (int): number of live neighbors of cell (row,column)
    '''

    # HINT: each cell has eight neighbors
    # If the cell has indices r,c then the neighbors have these indices
    #
    #  r-1,c-1    r-1,c    r-1,c+1
    #
    #  r,  c-1    r,  c    r,  c+1
    #
    #  r+1,c-1    r+1,c    r+1,c+1


    # HINT2: The grid is periodic (it wraps around).
    #       The left and right edges of the grid touch.
    #       The upper and lower edges of the grid touch.
    #
    #       Therefore, if a neighbor's row or column index
    #       becomes negative or too large, it must be adjusted
    #       by the number of rows or the number of columns.


    # TODO - Find the number of grid rows (HINT: use the len() of the grid)

    # TODO - Find the number of grid columns (HINT: use the len() of the first row)


    # TODO - Compute neighbor indices.
    #        Make sure all indices are positive!
    #        Make sure all indices are not too large!


    # TODO - Count the number of live neighbors.
    #        Do NOT count the cell in the middle, only neighbors!


    # TODO - Return the number of live neighbors

# -------------------------------------------------------------------------

# Write the body of the gridUpdate function.
#
# The Game of Life is played in turns.
# Each turn, the current grid (gridCurrent) is updated.
# Updates happen by looking at the previous grid (gridPrevious).
# For each grid cell, count that cell's live neighbors in the previous turn.
# Then set that cell's value (0 dead, 1 alive) in the current grid based
# on the rules of the Game of Life.
#
# 1. Any live cell with two or three live neighbours survives.
#
# 2. Any dead cell with three live neighbours becomes a live cell.
#
# 3. All other live cells die in the next generation. Dead cells stay dead.

def gridUpdate():
    '''
    Update the current game of life grid based on the previous grid.

        Parameters: no parameters

        Return Value: no return value
    '''

    # HINT: You must modify gridCurrent. Let the function know it is global.
    #       You will NOT modify gridPrevious but you will look at it.

    # HINT: The gridUpdate function should call the countLiveNeighbors function.

    # HINT: Use nested indexing for loops, not value for loops.
    #       Loop over grid rows, and for each row, loop over columns.


    # TODO - write the function's code here
    

    # this function does not return anything,
    # this return statement just ends the function
    return

# --------------------------------------------------------------------------

# Write the body of the playOneTurn function.
#
# You can assume when this function is called,
# both game grids are already created and the same size.

def playOneTurn():

    # TODO - Swap the grids.
    #        You should already have a function that does this!

    # TODO - Update the current grid.
    #        You should already have a function that does this!

    # TODO - Print the current grid (with symbols/letters, not numbers).
    #        You should already have a function that converts a grid to str.
    #        Print the string returned by that function.

    # TODO - Print a blank line.
    #        (there should be two blank lines after the grid is printed)

    # this function does not return anything,
    # this return statement just ends the function
    return

# --------------------------------------------------------------------------


# DO NOT WRITE ANY TEST CODE IN THIS MODULE FILE!
#
# If you want to write your own test code, write a separate test program.
# Import this module file into that test program.


# DO NOT WRITE A MAIN FUNCTION IN THIS MODULE FILE!
#
# This is a module only, not a full program.
# Main functions go only in full programs.
# The zyBooks tests in this lab contain full test programs
# that import your module file.
