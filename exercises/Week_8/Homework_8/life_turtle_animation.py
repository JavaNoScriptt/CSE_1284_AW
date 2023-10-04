# LAB Game of Life
# turtle animation

####################################################
#                                                  #
#           DO NOT MODIFY THIS FILE !!!            #
#                                                  #
####################################################

from time import sleep
from random import *
from turtle import *
import life_module



bWindowCreated = False

winWidth  = 800
winHeight = 800

def createTurtleWindow():
    global bWindowCreated

    setup( winWidth, winHeight, -50, 50 )
    title( "Game of Life" )
    bWindowCreated = True

    degrees()
    speed(0)
    hideturtle()
    tracer(0)
    delay(0)

# --------------------------------------------------------------------------

def drawSquare( sideLength, rgb ):
    pencolor( 'black' )
    fillcolor( rgb )
    begin_fill()
    for s in range(4):
        forward( sideLength )
        right(90)
    end_fill()

# --------------------------------------------------------------------------

def displayGrid_turtle( lifeStep ):

    global bWindowCreated

    if not bWindowCreated:
        createTurtleWindow()

    titleString = "Game of Life: step " + str(lifeStep)
    title( titleString )

    # IMPORTANT!!!
    # Always call clear at the beginning of each new animation frame.
    # Turtle keeps a list of drawing commands. Without clearing, this list
    # keeps growing longer. Without clearing, each frame redraws all
    # previous frames. Each frame thus takes longer and longer to draw.
    clear()

    grid = life_module.gridCurrent

    rowCount = len(grid)
    colCount = len(grid[0])

    ystep = -(winHeight - 20) // rowCount
    xstep = (winWidth - 20) // colCount

    #print( xstep, ystep ) # debug

    if xstep > ystep:
        ystep = -xstep
    else:
        xstep = -ystep

    offsetx =  1
    offsety = -1
    xstart = offsetx - (winWidth-20)/2
    ystart = offsety + (winHeight-20)/2

    y = ystart
    for row in grid:
        x = xstart
        for cell in row:
            rgb = [1,1,1]
            if cell != 0:
                rgb = [0.0,0.7,1]
                #rgb = cmap[cell]
            penup()
            #print( x, y )  # debug
            goto(x,y)
            pendown()
            drawSquare( xstep, rgb )
            x += xstep
        y += ystep
        
    update()

# --------------------------------------------------------------------------

# fill grids with zeros
# grids are row major, grid[row][col]
def zeroGrids( rowCount, colCount ):

    life_module.gridCurrent  = []
    life_module.gridPrevious = []

    grid    = life_module.gridCurrent
    gridOld = life_module.gridPrevious

    for row in range(rowCount):
        grid.append([])
        gridOld.append([])

        for col in range(colCount):
            grid[row].append(0)
            gridOld[row].append(0)

# --------------------------------------------------------------------------

# put some initial pattern(s) in the current grid
def initGrid( initPattern ):

    grid = life_module.gridCurrent
    
    # block in corner
    if initPattern == 'block':
        grid[0][0] = 1
        grid[0][1] = 1
        grid[1][0] = 1
        grid[1][1] = 1

    # blinker in center
    elif initPattern == 'blinker':
        grid[1][3] = 1
        grid[2][3] = 1
        grid[3][3] = 1
        
    # blinker in corner
    elif initPattern == 'blinkerCorner':
        grid[0][0] = 1
        grid[1][0] = 1
        grid[2][0] = 1

    # glider in corner
    elif initPattern == 'glider':
        grid[0][2] = 1
        grid[1][2] = 1
        grid[2][2] = 1
        grid[2][1] = 1
        grid[1][0] = 1

    # random
    elif initPattern == 'random':
        rowCount = len(grid)
        colCount = len(grid[0])

        for row in range(rowCount):
            for col in range(colCount):
                foo = randrange(5)
                if foo == 0:
                    grid[row][col] = 1

    # r-pentomino
    elif initPattern == 'r-pentamino':
        rowCount = len(grid)
        colCount = len(grid[0])

        midRow = int(rowCount/2)
        midCol = int(colCount/2)

        grid[midRow-1][midCol  ] = 1
        grid[midRow-1][midCol+1] = 1
        grid[midRow  ][midCol-1] = 1
        grid[midRow  ][midCol  ] = 1
        grid[midRow+1][midCol  ] = 1

    # pi-heptamino
    elif initPattern == 'pi-heptamino':
        rowCount = len(grid)
        colCount = len(grid[0])

        midRow = int(rowCount/2)
        midCol = int(colCount/2)

        grid[midRow-1][midCol-1] = 1
        grid[midRow-1][midCol  ] = 1
        grid[midRow-1][midCol+1] = 1
        grid[midRow  ][midCol-1] = 1
        grid[midRow  ][midCol+1] = 1
        grid[midRow+1][midCol-1] = 1
        grid[midRow+1][midCol+1] = 1

    # small flower, evolves into blinkers
    elif initPattern == 'flowerSmall':

        rowCount = len(grid)
        colCount = len(grid[0])

        r = int(rowCount/2)
        c = int(colCount/2)

        grid[r  ][c-2] = 1
        grid[r  ][c-1] = 1
        grid[r  ][c+1] = 1
        grid[r  ][c+2] = 1
        grid[r+1][c  ] = 1
        grid[r-1][c  ] = 1

        # - - -
##        grid[r-2][c  ] = 1
##        grid[r-1][c-1] = 1
##        grid[r-1][c+1] = 1
##        grid[r  ][c-2] = 1
##        grid[r  ][c+2] = 1
##        grid[r+1][c-1] = 1
##        grid[r+1][c+1] = 1
##        grid[r+2][c  ] = 1

        # - - -
        
##        grid[r-2][c-1] = 1
##        grid[r-2][c  ] = 1
##        grid[r-2][c+1] = 1
##
##        grid[r-1][c-2] = 1
##        grid[r  ][c-2] = 1
##        grid[r+1][c-2] = 1
##
##        grid[r-1][c+2] = 1
##        grid[r  ][c+2] = 1
##        grid[r+1][c+2] = 1
##
##        grid[r+2][c-1] = 1
##        grid[r+2][c  ] = 1
##        grid[r+2][c+1] = 1
        

    # large flower, evolves into tubs or boats or something
    elif initPattern == 'flowerLarge':

        rowCount = len(grid)
        colCount = len(grid[0])

        r = int(rowCount/2)
        c = int(colCount/2)

        grid[r-3][c  ] = 1

        grid[r-2][c-1] = 1
        #grid[r-2][c  ] = 1
        grid[r-2][c+1] = 1

        grid[r-1][c-2] = 1
        #grid[r-1][c-1] = 1
        #grid[r-1][c+1] = 1
        grid[r-1][c+2] = 1

        #grid[r  ][c-3] = 1
        grid[r  ][c-2] = 1
        #grid[r  ][c-1] = 1
        #grid[r  ][c+1] = 1
        grid[r  ][c+2] = 1
        #grid[r  ][c+3] = 1

        grid[r+1][c-2] = 1
        #grid[r+1][c-1] = 1
        #grid[r+1][c+1] = 1
        grid[r+1][c+2] = 1

        grid[r+2][c-1] = 1
        #grid[r+2][c  ] = 1
        grid[r+2][c+1] = 1

        grid[r+3][c  ] = 1

    # pulsar synthesis from glider and blocks
    elif initPattern == 'pulsarSynthesis':
        rowCount = len(grid)
        colCount = len(grid[0])

        midRow = int(rowCount/2) + 4
        midCol = int(colCount/2) - 1

        x = midCol - 3       # left block
        y = midRow + 1
        grid[y  ][x  ] = 1
        grid[y  ][x+1] = 1
        grid[y+1][x+1] = 1
        grid[y+1][x  ] = 1

        x = midCol + 1       # right block
        grid[y  ][x  ] = 1
        grid[y  ][x+1] = 1
        grid[y+1][x+1] = 1
        grid[y+1][x  ] = 1

        y = midRow - 2
        grid[y-1][x-1] = 1
        grid[y  ][x  ] = 1
        grid[y  ][x+1] = 1
        grid[y-1][x+1] = 1
        grid[y-2][x+1] = 1

    else:
        print( "unknown initial pattern:", initPattern )
        exit()
        
# ---------------------------------------------------------------------------
# main program

def main():

    print( "\nConway's Game of Life\n" )
    print( "1. random" )
    print( "2. r-pentamino" )
    print( "3. pi-heptamino" )
    print( "4. small flower -> blinkers" )
    print( "5. large flower -> beehives" )
    print( "6. blocks, glider -> pulsar" )
    print( "7. one glider" )
    print( '' )

    choice = input( "choose initial grid: " )
    print( '' )

    
    lifeStepCount = 255
    s = 0

    # 5,10 good for debugging, 60,60 looks nice, 86,86 slow

    if choice == '1':
        zeroGrids(86,86)  
        initGrid( 'random' )
        s = 0

    elif choice == '2':
        zeroGrids(60,60)
        initGrid( 'r-pentamino' )
        s = 0.1
        
    elif choice == '3':
        zeroGrids(60,60)
        initGrid( 'pi-heptamino' )
        s = 0.1

    elif choice == '4':
        zeroGrids(30,30)
        initGrid( 'flowerSmall' )
        lifeStepCount = 12
        s = 0.5

    elif choice == '5':
        zeroGrids(30,30)
        initGrid( 'flowerLarge' )
        lifeStepCount = 20
        s = 0.5

    elif choice == '6':
        zeroGrids(30,30)
        initGrid( 'pulsarSynthesis' )
        s = 0.5

    else:
        zeroGrids(30,30)
        initGrid( 'glider' )
        s = 0.3

    #zeroGrids(30,30)
    #initGrid( 'pulsarSynthesis' )
    #s = 0.4
    

    displayGrid_turtle( 1 )
    sleep( s )

    for lifeStep in range(2,lifeStepCount+1):

        life_module.gridSwap()
        life_module.gridUpdate()
        displayGrid_turtle( lifeStep )
        sleep( s )

    print( "all done" )



if __name__ == '__main__':
    main()
    done()



