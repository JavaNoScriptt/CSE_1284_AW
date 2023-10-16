# tuples and functions module file

# -------------------------------------------------------------

# do NOT modify this function

def isiterable( thingie ):
    '''
    check if something is iterable

    parameters:
        thingie - anything, an object, a literal, even None

    returns:
        True if iterable, False otherwise
    '''
    if thingie == None:
        return False
    
    try:
        iterator = iter(thingie)
        return True
    except:
        return False

# ------------------------------------------------------------

# write the body of this function

def getIntegerTupleFromData( data ):
    '''
    creates a tuple of all the integers in the data

    parameters:
        data - a container of data items, can be empty
               data must be an iterable type (list, tuple, or set)

    returns:
        tuple of integers from the data
    '''

    # ---------------------------------------
    # INT -> TUPLE
    # ---------------------------------------
    # 
    # if data is an instance of the integer type (int)
    #     return a tuple with that one integer   
    # 
    # -----------------------------------------------------
    # NON-ITERABLE -> TUPLE
    # -----------------------------------------------------
    # 
    # if data is NOT iterable
    #     return an empty tuple
    # 
    # ----------------------------------------------
    # ITERABLE -> TUPLE
    # ----------------------------------------------
    # 
    # if data is an instance of the string type (str)
    #     return an empty tuple
    # 
    # create an empty list of integers
    # 
    # for each item in the data 
    #     if the item is an instance of the integer type (int)
    #         append the item to the list of integers
    # 
    # if data is an instance of the set type
    #     sort the list of integers
    # 
    # convert the list of integers to a tuple
    #
    # return the tuple

    ans = []
    if type(data) == type(1):
        return(data,)
    elif isiterable(data) == False or data == None:
        return ()
    elif type(data) == type(''):
        return()
    else:
        for item in  data:
            if type(item) == type(1):
                ans.append(item)
            
        
        ans.sort()
        ans = tuple(ans)
        return ans
   
        

    
    


    
