# week 2 extra practice
# =====================



import math
import random


# problem 1 - root of 5
# ---------
root_of_5 = math.sqrt( 5.0 )    # fix this line
print( "problem 1:", root_of_5, "\n" )


# problem 2 - rolling dice
# ---------
# The die rolling code has two problems. Fix them.
# We want to roll die values between 1 and 6 inclusive.
print( "problem 2: ", end="" )
for counter in range(20):
    die_roll = random.randrange(1,6)                  # fix this line, 2 problems
    print( die_roll, end=" " )
print()


# problem 3 - coins
# ---------
# You have $1.05
# A quarter coin is worth $0.25 or 25 cents.
# How many quarter coins do you have?
# You also have a nickel (5 cents).
dollar_total = 1.05
quarter_value = 0.25
quarter_count = dollar_total // quarter_value  # replace with one of / // %
print( "problem 3:", int(quarter_count), "quarters\n" )


# problem 4 - shipping boxes
# ---------
# We want to ship some boxes but only if they are full!
# How many full boxes do we have?
# We can fit 8 widgets per box.
widgets_per_box = 8
total_widgets = 63
                                           # replace ??? with one of / // %
full_box_count = total_widgets // widgets_per_box
print( "problem 4: ", end="" )
print( full_box_count, "full boxes\n" )


# problem 5 - weight conversion
# ---------
# We want to convert a weight in pounds (lb)
# to a weight in kilograms (kg).
# We have pounds per kilo but we want kilo per pounds.
# To get kilo per pound, divide 1 by pounds per kilo.
pounds_per_kilo = 2.20462262
kilos_per_pound = 1.0 / pounds_per_kilo  # replace ??? with one of / // %
weight_lb = 150.23
weight_kg = weight_lb * kilos_per_pound
print( "problem 5:", f'{weight_lb:.2f}', "lb is", f'{weight_kg:.2f}', "kg\n" )


# problem 6 - bus stop
# ---------
# We have 4 buses and 145 passengers.
# Each bus has a capacity of 30 people.
# How many passengers can't get on a bus?
bus_count = 4
bus_capacity = 30
passenger_count = 145
passengers_left = passenger_count % bus_capacity  # replace ??? with / // %
print( "problem 6:", passengers_left, "passengers left\n" )


# problem 7 - fractional part of a number
# ---------
# We have a floating point number.
# We want to get its whole part (integer)
# and its fractional part (digits after the decimal)
number = 5.8429
whole_part = int(number)
frac_part = number % whole_part         # replace ??? with one of / // %
print( "problem 7: whole", whole_part, ", frac ", frac_part, "\n" )


# problem 8 - taxi stand
# ---------
# We have 17 people waiting for a taxi.
# Each taxi can hold 4 people.
# How many taxis do we need for ALL passengers?
# One taxi might not be full, that's okay.
passenger_count = 17
taxi_capacity = 4
                                          #  replace ??? with one of / // %
taxi_count = math.ceil( passenger_count / taxi_capacity )
print('problem 9:  ', taxi_count) #You said I coudl make this print statement

# problem 9 - MORE CATS!
# ---------
# When asked how many cats you have, type 3.
# Even if you have no cats, type 3 anyway.
cat_count = int(input( "problem 9: How many cats? " ))    # fix this line
print( cat_count * "cat ", "\n" )


# problem 10 - big cat?
# ----------
# Your cat is getting weighed at the vet.
# Display the cat's weight on a digital scale.
# When asked for the cat's weight, always type in 10.25
cat_weight = float(input( "problem 10: Cat weight (lb)? " ))   # this this line
print( "cat weight:", f'{cat_weight:.2f}', "lb\n" )


