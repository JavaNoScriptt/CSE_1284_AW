print('')
number = int(input("enter house number:   "))
address = input('enter street address: ')
print('')
print(f'''These are your neighbors' addresses on {address}
You are at the *

  _       _       _
 / \\     / \\     / \\
/   \\   / * \\   /   \\
|___|   |___|   |___|
 {number-2}     {number}     {number+2}

  _       _       _
 / \\     / \\     / \\
/   \\   /   \\   /   \\
|___|   |___|   |___|
 {number-1}     {number+1}     {number+3}
''')
