# checks if something is an int or float, returns True/False
def isnumber( something ):

    if isinstance( something, int ):
        return True

    if isinstance( something, float ):
        return True

    return False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
NONZERO_AMOUNT_ONLY = 0
ZERO_AMOUNT_ONLY    = 1
ALL_ITEMS           = 2

class Item:
    def __init__(self, cost, name):

        self.cost = cost
        self.name = name

class ItemContainer:
    def __init__(self, a_name='items'):
        if not isinstance(a_name, str):
            raise Exception("Name must be a string")
        self.__name = a_name
        self.__items = {}

    def __str__(self, what_to_show=NONZERO_AMOUNT_ONLY):
        if not self.__items:
            return self.__name + ":\n"
        items_to_show = []
        for item, amount in sorted(self.__items.items(), key=lambda x: x[0].name):
            if (what_to_show == NONZERO_AMOUNT_ONLY and amount > 0) or (what_to_show == ZERO_AMOUNT_ONLY and amount == 0) or (what_to_show == ALL_ITEMS):
                items_to_show.append(f"{amount:4}   ${item.cost:.2f} {item.name}")
        return self.__name + ":\n" + "\n".join(items_to_show) +"\n"

    def print_items(self, what_to_show=NONZERO_AMOUNT_ONLY):
        print(self.__str__(what_to_show))

    def get_name(self):
        return self.__name

    def set_name(self, a_name):
        if not isinstance(a_name, str):
            raise Exception("Name must be a string")
        self.__name = a_name

    def add_item(self, an_item):
        if not isinstance(an_item, Item):
            raise Exception("Item must be an instance of Item class")
        self.__items[an_item] = self.__items.get(an_item, 0) + 1

    def add_items(self, an_item, amount):
        if not isinstance(an_item, Item):
            raise Exception("Item must be an instance of Item class")
        if not isinstance(amount, int):
            raise Exception("Amount must be an integer")
        self.__items[an_item] = self.__items.get(an_item, 0) + amount

    def remove_item(self, an_item):
        if not isinstance(an_item, Item):
            raise Exception("Item must be an instance of Item class")
        if self.__items.get(an_item, 0) <= 0:
            raise Exception("Item cannot be removed because amount would be less than zero")
        self.__items[an_item] -= 1

    def remove_items(self, an_item, amount):
        if not isinstance(an_item, Item):
            raise Exception("Item must be an instance of Item class")
        if not isinstance(amount, int):
            raise Exception("Amount must be an integer")
        if self.__items.get(an_item, 0) < amount:
            raise Exception("Items cannot be removed because amount would be less than zero")
        self.__items[an_item] -= amount

    def get_entry_count(self):
        return len(self.__items)

    def get_total_item_count(self):
        return sum(self.__items.values())

    def get_total_item_cost(self):
        return sum(item.cost * amount for item, amount in self.__items.items())





# --------------------------------------------------------------

#################################
#                               #
# DO NOT MODIFY BELOW THIS LINE #
#                               #
#################################

# for testing/debugging
def main():

    # get some item cost and names from the user
    cost1 = float( input( "cost1: " ) )
    name1 = input( "name1: " )
    
    cost2 = float( input( "cost2: " ) )
    name2 = input( "name2: " )
    
    cost3 = float( input( "cost3: " ) )
    name3 = input( "name3: " )

    print( '' )

    # create three items
    item1 = Item( cost1, name1 )
    item2 = Item( cost2, name2 )
    item3 = Item( cost3, name3 )

    # put items in a list
    items = [ item1, item2, item3 ]

    # print list
    for item in items:
        print( item )
    print( '' )
    
    # sort the list
    items.sort()

    # print sorted list
    for item in items:
        print( item )
    print( '' )
    

if __name__ == '__main__':
    main()
