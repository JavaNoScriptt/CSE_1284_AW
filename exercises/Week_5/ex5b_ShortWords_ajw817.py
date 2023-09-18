words = []
asked = ''

for x in range(0,5):
    asked = input('Give me a 3 letter word!!\t')
    while len(asked) != 3:
        print('That is not a 3 letter word. Try Again')
        asked = input('Give me a 3 letter word!!\t')
    words.append(asked)
print(words)