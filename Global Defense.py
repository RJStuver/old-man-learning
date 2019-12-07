#Global Defense

aliens = 2
password = 'ALIENS'

print('Quickly! Aliens are invading the planet.')
print('You need to activate the global defense platforms.')
print('Hope you know the password, for Earth;s sake')
print()
print('--------------------------------------------------')
print('      WELCOME TO THE GLOBAL DEFENSE NETWORK       ')
print('--------------------------------------------------')
print()

guess = input('Please enter the password: ').upper()

while guess != password:
    print()
    print('INCORRECT PASSWORD')
    print()

    aliens = aliens**2
    print('There are', aliens,'aliens now on Earth.  Try again.')

    if aliens > 74000000000:
        break

    print()
    print('Password hint:  the things that are attacking us.')
    print()
    guess = input('quick!  Please enter the password. ').upper()

if aliens > 74000000000:
    print('Noooooo! The aliens have otnumbered us.  All is lost')
else:
    print('Hooray!  We won the fight and the world is saved!')





    

          
