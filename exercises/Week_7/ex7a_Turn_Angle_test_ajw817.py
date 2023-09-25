from ex7a_Turn_Angle_module_ajw817 import intAngle


testSides = [3,4,5,6]
expectedAns =[120,90,72,60]
actual = []

for i in testSides:
    actual.append(intAngle(i))


print(actual)