stop =7
result = 0
for a in range(2):
    print(a, end=': ')
    for b in range(4):
        result += a + b
        if result > stop:
            print('-', end=' ')
            continue
        print(result, end=' ')
    print()