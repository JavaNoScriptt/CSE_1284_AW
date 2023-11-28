def isnumber( something ):
    if isinstance( something, int ):
        return True
    if isinstance( something, float ):
        return True
    return False


class Item():
    def __init__(self,cost,name):
        if not isinstance( name, str ):
            raise ValueError( "Item.set_name, name must be str type" )
        if not isnumber(cost):
            raise ValueError("Item.set_name, name must be str type")
        self.__cost = float(cost)
        self.__name = str(name)
        pass
    def __str__(self):
        return f'${self.__cost:.2f} {self.__name}'
    def get_cost(self):
        return self.__cost
    def get_name(self):
        return self.__name
    def set_cost(self,cost):
        if not isnumber(cost):
            raise ValueError("Item.set_name, name must be str type")
        self.__cost = float(cost)
        
    def set_name(self,name):
        if not isinstance( name, str ):
            raise ValueError( "Item.set_name, name must be str type" )
        self.__name = str(name)
    def __gt__(self,other):
        if self.__name > other.__name:
            return True
        return False


def create_item(cost,name):


    to_add = Item(cost,name)

    return to_add





def print_items( item_list ):

    for item in item_list:
        print( item )


def main():
    price1 = float(input('cost1: '))
    item1 = input('name1: ')
    price2 = float(input('cost2: '))
    item2 = input('name2: ')
    price3 = float(input('cost3: '))
    item3 = input('name3: ')
    stuff = [ Item( price1, item1), Item( price2, item2 ), Item( price3, item3) ]
    print(f'\n${stuff[0].get_cost()} {stuff[0].get_name()}\n${stuff[1].get_cost()} {stuff[1].get_name()}\n${stuff[2].get_cost()} {stuff[2].get_name()}',end='\n\n')
    stuff.sort()
    print(f'${stuff[0].get_cost()} {stuff[0].get_name()}\n${stuff[1].get_cost()} {stuff[1].get_name()}\n${stuff[2].get_cost()} {stuff[2].get_name()}',end='\n\n')




if __name__ == '__main__':
    main()


