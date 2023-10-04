from ex7a_turn_angle_module_ajw817 import angle
import turtle as turt

turt.title('yay')
turt.screensize(800,600)
turt.speed(100)

turt.penup()
turt.goto(-300,0)
turt.pendown()
testSides = [3,4,5,6]
expectedAns =[120,90,72,60]
actual,passing = [],[]
right,count =0,0
for sides in testSides:
    actual.append(angle(sides))
for i in expectedAns:
    if i == actual[count]:
        right+=1
        passing.append('Pass')
    else:
        passing.append('Fail')
    count+=1
print('''
Test programer name: Alex Woods
module programer name: Benjamin Conway
''')
print(f'''                           expected                    computed
num sides         turn angle (deg)        turn angle (deg)           test passed?
{testSides[0]}                        {expectedAns[0]}                  {actual[0]}                     {passing[0]}
{testSides[1]}                        {expectedAns[1]}                   {actual[1]}                     {passing[1]}
{testSides[2]}                        {expectedAns[2]}                   {actual[2]}                     {passing[2]}
{testSides[3]}                        {expectedAns[3]}                   {actual[3]}                     {passing[3]}

{right}/4 tests passed

''')


for side in testSides:
    for i in range(0,side):
        turt.forward(100) # could make this apart of the function requirements to add more functionalities
        turt.left(actual[side-3])
    turt.penup()
    turt.forward(150)
    turt.pendown()
