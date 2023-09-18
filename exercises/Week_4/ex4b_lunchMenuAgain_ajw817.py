#Lunch menu with list
#Basic objective is to learn list
options = [1,2,3,4,5,6,7,8]
item_price = [9.50 , 7.75 ,6.75, 8.25, 7.50, 6.15, 9.25,6.00]
item = ['Hamburger Special','Shrimp and Grits','Sassy Salad','Chicken Croissant','Falafel Plate','Pita and Hummus','Fresh Sushi','Soup of the Day']

print('''Lunch Menu
      
1 - $9.50 Hamburger Special
2 - $7.75 Shrimp and Grits
3 - $6.75 Sassy Salad
4 - $8.25 Chicken Croissant
5 - $7.50 Falafel Plate
6 - $6.15 Pita and Hummus
7 - $9.25 Fresh Sushi
8 - $6.00 Soup of the Day
      ''')

selection = int(input("What would you like for lunch? "))
print('') 
if selection in options:
    print(f"""You Ordered the {item[selection-1]}\nThat will be ${item_price[selection-1]+0.15*item_price[selection-1]} please
price {item_price[selection-1]}
gratuity {0.15*item_price[selection-1]}
TOTAL {item_price[selection-1]+0.15*item_price[selection-1]}""")

else:
    print('That is not a valid option')
