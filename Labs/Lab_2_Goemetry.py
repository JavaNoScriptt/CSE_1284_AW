x = int(input("Enter the x coordinate for the lower left corner of the rectangle:\t"))
y = int(input("Enter the y coordinate for the lower left corner of the rectangle:\t"))
print('')
rectangle_width = int(input("Enter the width of the rectangle:\t"))
height = int(input("Enter the height of the rectangle:\t"))
print('')
check_x = int(input('Enter the x coordinate of the point:\t'))

check_y = int(input('Enter the y coordinate of the point:\t'))
print()
lower_left = [x,y]
upper_left = [x,y+height]
lower_right =  [x+rectangle_width,y]
upper_right = [x+rectangle_width,y+height]


if (check_x >= lower_left[0] and check_x <= lower_right[0]) and (check_y == lower_left[1] or check_y == lower_right[1]):
    print('On the rectangle')
elif (check_y >= lower_left[1] and check_y <= upper_left[1]) and (check_x == lower_left[0] or check_x == lower_right[0]):
    print('On the rectangle')
else:
    print('Inside the rectangle')