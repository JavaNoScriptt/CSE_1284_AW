import turtle as turt

s = turt.getscreen()
t = turt.Turtle()

#Brings the turtle to a certian position without leaving pen marks
t.penup()
t.goto(-100,100) # could make a function tot teleport the turtle
t.pendown()


#This is a way ot do this problem with fucntions
'''
# makes the funtion to draw any shape based on sides alone
def draw(sides):
    angle = int(360/sides) # gets the interior angle of the shape
    if sides == 5:
        t.pencolor('Red')
    else:
        t.pencolor('Blue')
    
    # main part of the program where the sides are drawn
    for i in range(0,sides):
        t.forward(40) # could make this apart of the function requirements to add more functionalitys
        t.left(angle)

draw(5) # Drawing a pentagon

t.penup()
t.goto(-200,100) 
t.pendown()

draw(6) # Drawing a hexagon
'''
#Draws the pentagon in red
angle = 360/5
t.pencolor('Red')
for i in range(0,5):
        t.forward(40) # could make this apart of the function requirements to add more functionalitys
        t.left(angle)

t.penup()
t.goto(-200,100) 
t.pendown()


# Draws the hexagon in blue
angle = 360/6
t.pencolor('Blue')
for i in range(0,6):
        t.forward(40) # could make this apart of the function requirements to add more functionalitys
        t.left(angle)