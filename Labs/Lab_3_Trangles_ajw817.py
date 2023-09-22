import math

side1 = int(input())
side2 = int(input())
side3 = int(input())

sides = [side1,side2,side3]

sides.sort()
if math.sqrt(sides[0]**2 + sides[1]**2) == sides[2]: #Only right triangle obey the quadratic formula
    print('These lengths form a right triangle')
elif sides[0]+sides[1] > sides[2]: #non right triangle test
    print('These lengths form a triangle')
else:
    print('These lengths do not form a triangle')