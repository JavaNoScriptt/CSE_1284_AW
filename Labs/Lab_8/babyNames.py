


def getRank(file,name,gender):



    pass


def getGender():
    ans = input('Enter selection:  ')
    while True:
        try:
            ans = int(ans)
            if ans in (1,2):
                return ans
            else:
                raise TypeError


        except TypeError:
            print('ERROR:  must enter a 1 or a 2')
            ans = input('Please re-enter:  ')
            


    

def getName():
    ans = input('Enter the baby name you wish to research:  ')
    return ans



def main():
    name = getName()
    gender = getGender()

    pass






if __name__ == '__main__':
    main()