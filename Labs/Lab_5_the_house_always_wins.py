import random
random.seed(5)

def main():
    
    profitGoal = int(input('Profit Goal: '))
    money = int(input('Starting money: '))
    tblMin = int(input('Table minimum bet: '))
    tblMax = int(input('Table maximum bet: '))
    bet = tblMin
    tot_spins = 0
    print(f'Starting Money: {money}')
    while money >0 and money < profitGoal:
        
        spin = random.randint(0,36)
        if bet > money:
                bet = tblMin
        #print(spin, money, bet, win)     
        if spin%2==1:
            money+=bet
            print(f'Spin: {spin}. You won ${bet} on the bet. You had {money-bet}. Now you have {money} left.')
            bet = tblMin
            #print(spin, money, bet, win)   
        else:
            money -= bet
            print(f"Spin: {spin}. You lost ${bet} on the bet. You had {money+bet}. Now you have {money} left.")  
            bet = bet*2
            #print(spin, money, bet, win)   
            if bet > money:
                bet = tblMin
                #if bet*2 < money:
                #    bet *= 2
        #print(spin, money, bet, win)      
                

        
        tot_spins +=1

    if money <=0:
        print('You ran out of money')
    else:
        print(f'You reached your goal and beat the casino. You should stop now. You have ${money}.')


if __name__ == '__main__':
    main()