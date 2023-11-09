


def getRank(file,name,gender):
    try:
        with open(file, 'r') as file:
            for i in range(3):
                next(file)
            for line in file:
                parts = line.strip().split('	')

                if gender == 1:
                    if parts[1].lower() == name.lower():
                        return parts[0]
                else:
                    if parts[3].lower() == name.lower():
                        return parts[0]

        return "Not ranked"
    except FileNotFoundError:
        return "Not ranked"
    except IndexError:
        return "Not ranked"


    pass


def getGender():
    print("Which gender list do you wish to research?\n1. Male\n2. Female")
    ans = input('Enter selection:  ')
    while True:
        try:
            ans = int(ans)
            if ans in (1,2):
                return ans
            else:
                raise ValueError


        except ValueError:
            print('ERROR:  must enter a 1 or a 2')
            ans = input('Please re-enter:  ')
            


    

def getName():
    ans = input('Enter the baby name you wish to research:  ')
    return ans



def main():
    name = getName()
    gender = getGender()


    print("\nFor name:", name.capitalize())
    print("Decade Rank")
    print("======  ==========")

    # Loop through decades from 1900 to 1990
    for year in range(1900, 2000, 10):
        file_name = "NamesOf" + str(year) + "s.txt"
        rank = getRank(file_name, name, gender)
        print(year, rank)

    pass

if __name__ == '__main__':
    main()