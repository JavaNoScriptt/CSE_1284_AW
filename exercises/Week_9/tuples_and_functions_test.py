# tuples and functions test program

from tuples_and_functions_module import *


def doTest( data, expect ):
    result = getIntegerTupleFromData( data )
    passed = "passed" if expect == result else "FAILED"
    print( "data:   " + str(data) )
    print( "type:   " + str(type(data)) )
    print( "expect: " + str(expect) )
    print( "result: " + str(result) )
    print( "test " + passed )
    print( '' )



# single integer data
data = 5
expect = tuple([5])
doTest( data, expect )

# float data
data = 2.8
expect = ()
doTest( data, expect )

# None
data = None
expect = ()
doTest( data, expect )

# string data
data = "banana"
expect = ()
doTest( data, expect )

# list data
data = [1, "pickle", 2, (5,6,7), "kittens", 5.7, 3, 18.0]
expect = (1,2,3)
doTest( data, expect )

# tuple data
data = (7.2, 10, 20, "cookie", 30, [5,6,7], 40)
expect = (10,20,30,40)
doTest( data, expect )

# set data
data = {400, "doughnut", 5.9, 200, 300, (5,6,7), 100}
expect = (100,200,300,400)
doTest( data, expect )


