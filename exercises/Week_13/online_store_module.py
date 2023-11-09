


class Item():
    def __init__(self,cost,name):

        self.cost = float(cost)
        self.name = str(name)
        pass
    def __str__(self):
        return f'${self.cost:.2f} {self.name}'

def create_item(cost,name):


    to_add = Item(cost,name)

    return to_add





def print_items( item_list ):

    for item in item_list:
        print( item )





