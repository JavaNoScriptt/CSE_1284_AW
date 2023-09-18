gal = float(input('vehicle gas tank capacity (gl)? '))

miles = float(input('max driving distance on one tank (mi)? '))

print('')

mpg = miles/gal

print(f'vehcile gas mileage: {mpg:.2f} mpg')

if mpg >37.0:

    print('vehicle exceeds company requirements')

elif mpg >= 29.5 and mpg <= 37.0:

    print('vehicle meets company requirements')

elif mpg < 29.5 and mpg >=8 :

    print('vehicle does not meet company requirements')

else:

    print('vehicle is not legal to drive in the state')