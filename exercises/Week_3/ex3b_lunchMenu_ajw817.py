#Lunch menu with if/else branches
#Basic objective is to learn if/else branches
print('''Lunch Menu
      
a - $9.50 Hamburger Special
b - $7.75 Shrimp and Grits
c - $6.75 Sassy Salad
d - $8.25 Chicken Croissant
e - $7.50 Falafel Plate
f - $6.15 Pita and Hummus
g - $9.25 Fresh Sushi
h - $6.00 Soup of the Day
      ''')

selection = input("What would you like for lunch? ")
print('') # 
if selection.lower() == 'a':
    print("You Ordered the Hamburger Special\nThat will be $9.50 please")
elif selection.lower() == 'b':
    print("You Ordered the Shrimp and Grits\nThat will be $7.75 please")
elif selection.lower() == 'c':
    print("You Ordered the Sassy Salad\nThat will be $6.75 please")
elif selection.lower() == 'd':
    print("You Ordered the Chicken Croissant\nThat will be $8.25 please")
elif selection.lower() == 'e':
    print("You Ordered the Falafel Plate\nThat will be $7.50 please")
elif selection.lower() == 'f':
    print("You Ordered the Pita and Hummus\nThat will be $6.15 please")
elif selection.lower() == 'g':
    print("You Ordered the Fresh Sushi\nThat will be $9.25 please")
elif selection.lower() == 'h':
    print("You Ordered the Soup of the Day\nThat will be $6.00 please")
else:
    print('That is not a valid option')