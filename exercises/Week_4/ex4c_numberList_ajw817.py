# Number list
enter , numList =275,[] # makes the start of the loop true and makes the list at the same time
print("""Enter a number to put it in a list
      enter a 0 or -1 to stop entering numbers""")
while enter >0:
    enter =  int(input("Enter a number: "))
    if enter > 0:
        numList.append(enter)
print('List of numbers')
print(numList)


