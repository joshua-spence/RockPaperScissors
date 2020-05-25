
# def output(a):
#     item = input('>')

#     if item == 'rock':
#         print('Sorry, computer chose scissors')
#         a = True
#     elif item == 'paper' or item == 'scissors':
#         print('Sorry, compute chose rock')
#         a = True
#     else: a = False

#     return a
    
    
# a = True    
# while a:
#     a = output(a)
# print('Goodbye')


import random
game = True

with open ('rating.txt','r') as f:
    f_contents = f.read()
gamers = list(f_contents.split(" ")) 


name = input('Enter your name: ')
print('Hello, ', name)

while game is True:

    item = input('')
    options = ['rock', 'scissors', 'paper']
    comp = (random.choice(options))
    
    if item == 'exit!': 
        print('Bye')
        break

    elif item == '!rating':
        check_name = name in gamers 
        if check_name is True:
            index = gamers.index(name)
            score = gamers[index+1]
            int(score)
        else: 
            score = 0



    else:
        if comp == item: print('There is a draw (%s)'% (comp) )
        elif comp == 'scissors' and item == 'rock': print('Well done. The computer chose %s and failed'% (comp))
        elif comp == 'rock' and item == 'paper': print('Well done. The computer chose %s and failed'% (comp))
        elif comp == 'paper' and item == 'scissors': print('Well done. The computer chose %s and failed'% (comp)) 

        elif comp == 'paper' and item == 'rock': print('Sorry, but the computer chose rock')
        elif comp == 'scissors' and item == 'paper': print('Sorry, but the computer chose rock')
        elif comp == 'rock' and item == 'scissors': print('Sorry, but the computer chose rock')
        
        else: print('Invalid input')

# ratings = open('rating.txt','w')
# ratings.write('Tim 350 Jane 200 Alex 400')
# ratings.close



name = input('Enter your name: ')
print('Hello, ',name)
check_name = name in gamers 

if check_name is True:
    index = gamers.index(name)
    score = gamers[index+1]
    int(score)
else: 
    score = 0




