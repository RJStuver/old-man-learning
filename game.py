#game

print('You are in a dark room in a mysterious castle.')
print('In front of you are three doors.  You must choose one.')
playerchoice = input('Choose 1,2, or 3, or Q   ')

if playerchoice == '1':  
        print('You find a room full of treasure.  you are now rich.')
        print('YOU WIN.')

elif playerchoice == '2':
    print('Angry ogre')
    print('You lose')

elif playerchoice == '3':
    print('sleeping dragon')
    print('You lose')
elif playerchoice == 'Q':
    exit()    

else:    
    print('Sorry, you did not choose 1, 2, or 3')

print('Run  game again')

     
