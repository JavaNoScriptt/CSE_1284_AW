
'''


dict= {
    user_name : [name, (Trusted_ips)]



}




'''
def read_user_data( filename ):
    '''
    Reads a user data file with the given name.
    Stores user data for later use.

    parameters: filename (str)

    returns: True - file read successfully
             False - file not read successfully
    '''
    try:
        with open(filename,'r') as file:
            user_data = {}
            
            
            lines = file.readlines()

            userID = ''
            userName = ''
            trustIP = []

            for i in lines:
                i = i.strip()
                if i:
                    if not userID:
                        userID = i
                    elif not userName:
                        userName = i
                    else:
                        trustIP.append(i)
                else:
                    if userID:
                        user_data[userID] = (userName,trustIP)
                        userID = ''
                        userName = ''
                        trustIP = []

            read_user_data.user_data = user_data
            
            return True
    except:
        return False



def does_ip_address_belong_to_user( check_ip, userID ):
    '''
    Does the ip address belong to the user with this user ID?

    parameters: check_ip (str), userID (str)

    returns: True - ip address belongs to user
             False - ip address does not belong to user
    '''
    if hasattr(read_user_data, 'User_data'):
        return False
    

    if userID in read_user_data.user_data:
        user_name, trusted_ips =read_user_data.user_data[userID]
        if check_ip in trusted_ips:
            return True
        
    return False



if __name__ == '__main__':

    
    checkIP = input()
    UssrID = input()
    print(read_user_data('user data.txt'))

    print(does_ip_address_belong_to_user(checkIP,UssrID))
    
