import turtle as turt

s = turt.getscreen()
t = turt.Turtle()
turt.title('Hwk 6c Laser Cutter ajw817')
turt.screensize(800,600)

# has a list of cordinates for the turtle to move through
cord_hex =[(-325,275),(-325,175),(-325,75),(-325,-25),(-325,-125)]
#different shapes have a different 
cord_penta = [] 

def teleport(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#This is a way to make shapes with a function
def draw(sides):
    angle = int(360/sides) # gets the interior angle of the shape
    if sides == 5: # for the different colors
        t.pencolor('Black')
    else:
        t.pencolor('Blue') 
    # main part of the program where the sides are drawn
    for i in range(0,sides):
        t.forward(45) # could make this apart of the function requirements to add more functionalitys
        t.right(angle)
        
#Draws all of the hexagons
for i in cord_hex:
    teleport(i[0],i[1])
    draw(6)
    

