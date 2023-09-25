user_text = input()
excluded = [' ',',','.','!']
counter = 0
for i in user_text:
    if i not in excluded:
        counter += 1
print(counter)