# Car diagnostics (Ifs within Ifs)
# The basic objective of this assignment is to learn about if branching

# Problem statement: 
'''
Today's car mechanics use sophisticated software diagnostic tools to determine what is wrong with a car.
We will implement a slightly less sophisticated diagnostic tool. Like the real thing, ours will recommend
possible fixes for the problem.
'''

problem = input("What is the Problem?  ")

if problem == 'Smell':
    smell = input('Where is the smell coming from? ')
    if smell =="Backseat":
        print('Remove the melted icecream from the backseat')
    elif smell == 'AC Unit':
        print('Change the air filter')
    else:
        print('That is not a valid option...')
elif problem == 'Noise':
    noise = input('What is the noise? ')
    if noise =="Thumping":
        print('Hit it with a hammer!!')
    elif noise == 'Clunking':
        print('Hit it with a spanner!!')
    elif noise =='Hissing':
        print('Remove the grumpy opossum hiding in the trunk!!')
    else:
        print("That is not a valid option...")
else:
    print('That is not a valid option')