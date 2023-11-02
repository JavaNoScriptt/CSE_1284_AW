


def main():
    text = input('file name? ')
    try:
        file = open(text,'r')
        print('''
Shopping List
''')
        for line in file:
            print(line, end='')
        file.close()
    except:
        print(f'\nERROR: file {text} could not be read')






if __name__ == '__main__':
    main()