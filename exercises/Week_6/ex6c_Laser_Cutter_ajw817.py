import turtle as turt

turt.title('Hwk 6c Laser Cutter ajw817')
turt.screensize(800,600)
turt.speed(100)
# has a list of cordinates for the turtle to move through
cord_hex =[(-325,275),(-325,175),(-325,75),(-325,-25),(-325,-125),(-325,-225),
           (-225,300),(-225,200),(-225,100),(-225,0),(-225,-100),(-225,-200),
           (-125,275),(-125,175),(-125,75),(-125,-25),(-125,-125),(-125,-225),
           (-25,300),(-25,200)]
#different shapes have a different cordinates
cord_penta = [(-25,50),(-25,-50),
              (75,300),(75,200),(75,100),(75,0),(75,-100),(75,-200),
              (175,300),(175,200),(175,100),(175,0),(175,-100),(175,-200)] 
# Makes a function to bring the turtle to somewhere without pens
def teleport(x,y):
    turt.penup()
    turt.goto(x,y)
    turt.pendown()
#This is a way to make shapes with a function
def draw(sides):
    angle = int(360/sides) # gets the interior angle of the shape
    if sides == 5: # for the different colors
        turt.pencolor('Black')
    else:
        turt.pencolor('Blue') 
    # main part of the program where the sides are drawn
    for i in range(0,sides):
        turt.forward(45) # could make this apart of the function requirements to add more functionalitys
        turt.right(angle)

        
#Draws all of the hexagons

for i in cord_hex:
    teleport(i[0],i[1])
    draw(6)

for i in cord_penta:
    teleport(i[0],i[1])
    draw(5)

