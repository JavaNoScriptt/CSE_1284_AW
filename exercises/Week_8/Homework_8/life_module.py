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
    for i in grid:
        # for each cell in the row, convert the cell
        for x in i:
            # add symbol to the string for this cell
            #   symbol + for cells that hold a zero
            if x == 0:
                bruh +='+'
            #   letter O for cells that are non-zero
            else:
                bruh += 'O'
            
        # add a newline to the string at the end of the grid row
        bruh += '\n'
        
    # return the string representation of the grid
    return bruh

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
    global gridPrevious
    # TODO - swap gridCurrent with gridPrevious
    #
    # HINT: Do NOT swap individual cell values! That's inefficient!
    #       Just swap the references to the whole 2D grids.
    gridPrevious , gridCurrent = gridCurrent, gridPrevious
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
    rows = len(grid) 
    # TODO - Find the number of grid columns (HINT: use the len() of the first row)
    columns = len(grid[0])

    # TODO - Compute neighbor indices.
    #        Make sure all indices are positive!
    #        Make sure all indices are not too large!
    upperL = grid[rowIndex-1][columnIndex-1]
    middleL =  grid[rowIndex%rows][columnIndex-1]
    lowerL = grid[(rowIndex+1)%rows][columnIndex-1]
    upperM = grid[rowIndex-1][columnIndex%columns]
    lowerM = grid[(rowIndex+1)%rows][columnIndex%columns]
    upperR  =grid[rowIndex-1][(columnIndex+1)%columns]
    middleR  =grid[rowIndex%rows][(columnIndex+1)%columns]
    lowerR  =grid[(rowIndex+1)%rows][(columnIndex+1)%columns]


    # TODO - Count the number of live neighbors.
    #        Do NOT count the cell in the middle, only neighbors!
    ans = upperL + upperM + upperR + middleL + middleR + lowerL + lowerM + lowerR

    # TODO - Return the number of live neighbors
    return ans
# -------------------------------------------------------------------------
'''


rows =4
row = [0,1,2,3]
rowindex = 


'''

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
    
    # 1. Any live cell with two or three live neighbours survives.
#
# 2. Any dead cell with three live neighbours becomes a live cell.
#
# 3. All other live cells die in the next generation. Dead cells stay dead.

    global gridCurrent
    rows = len(gridPrevious[0])
    coll = len(gridPrevious)
    for row in range(0,rows):
            
            for columns in range(0,coll):
                
                liveNeighbors = countLiveNeighbors(gridPrevious, columns, row)

                if gridPrevious[columns][row] == 1:
                    if liveNeighbors==2 or liveNeighbors == 3:
                        gridCurrent[columns][row] = 1
                    else:
                        gridCurrent[columns][row] = 0
                else:
                    if liveNeighbors == 3:
                        gridCurrent[columns][row] = 1
                    #else:
                    #   gridCurrent[columns][row] = 0
                '''
                if gridPrevious[row][x] == 1 and (liveNeighbors==2 or liveNeighbors == 3):
                    gridCurrent[row][x] = 1 
                if gridPrevious[row][x] == 0 and liveNeighbors == 3:
                    gridCurrent[row][x] = 1
                if gridPrevious[row][x] == 1 and (liveNeighbors!=2 or liveNeighbors != 3):
                    gridCurrent[row][x] = 0
                '''
                
                
    
    
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
    gridSwap()
    # TODO - Update the current grid.
    #        You should already have a function that does this!
    gridUpdate()
    # TODO - Print the current grid (with symbols/letters, not numbers).
    #        You should already have a function that converts a grid to str.
    #        Print the string returned by that function.
    print(gridToString(gridCurrent))
    # TODO - Print a blank line.
    #        (there should be two blank lines after the grid is printed)
    print('')
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

