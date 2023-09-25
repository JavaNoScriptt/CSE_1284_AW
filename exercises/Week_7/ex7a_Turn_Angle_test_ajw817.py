from ex7a_Turn_Angle_module_ajw817 import intAngle


testSides = [3,4,5,6]
expectedAns =[120,90,72,60]
actual, = []
right,count =0,0
for sides in testSides:
    actual.append(intAngle(sides))
for i in expectedAns:
    if i == actual[0]:
        right+=1
    count+=1

print(f'''                           expected                    computed
num sides         turn angle (deg)        turn angle (deg)           test passed?
{testSides[0]}                        {expectedAns[0]}                            120                               pass
{testSides[1]}                          {expectedAns[1]}                              90                                pass
{testSides[2]}                          {expectedAns[2]}                              72                                pass
{testSides[3]}                          {expectedAns[3]}                              60                                pass

{right}/4 tests passed

''')
