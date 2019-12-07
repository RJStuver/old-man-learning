#game

import random

print('You are in a dark room in a mysterious castle.')
print('In front of you are four doors.  You must choose one.')

playerchoice = input('Choose 1,2,3 or 4''   ')

if playerchoice == '1':  
    print('You find a room full of treasure.  you are now rich.')
    print('YOU WIN.')

elif playerchoice == '2':
    print('Angry ogre')
    print('You lose')

elif playerchoice == '3':
    print('sleeping dragon')
    print('You can either:')

    print('1) Try to steal some gold.')
    print('2) Try to sneak around the dragonn to the exit')      
    
    dragonchoice = input('Type 1 or 2 ...')
    
    if dragonchoice == '1':
        print('The dragon eats you.')
        print('GAME OVER.  YOU LOOSE')
            
    elif dragonchoice == '2':        
        print('You escape')
        print('Game over.  You win')
        
    else:   
        print('Sorry, you did not enter 1 or 2!')
        
elif playerchoice == '4':              
    print('you enter a room with a sphinx.')
    
    number = int(input('Pick a number 1 to 10    '))
    if number == random.randint(1,10):
        print('you must go free')
    else:
        print('Incorrect')
        print('GAME OVER.  YOU LOSE.')
    
       
         

