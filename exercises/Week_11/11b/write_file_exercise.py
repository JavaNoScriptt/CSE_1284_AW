


def main():


    file_name = input('file name? ')

    file = open(file_name, "w")
    print('\nEnter shopping list items.\nPress ENTER when finished.')
    text = input('? ')
    while text != '':
        file.write(text + '\n')
        text = input('? ')
        


    file.close()
    return













