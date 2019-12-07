#Alphabet
alphabet = 'ABCDEFGHIJLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
stringToEncrypt = (input('Please enter a message to encrypt '))
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input('Pliese enter a whole number frin 1-25 to be your key'))

encryptedString = ''
for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    if currentCharacter in alphabet:
        encryptedString = encryptedString + alphabet[newPosition]

    else:
        encryptedString = encryptedString + currentCharacter
print('Your encrypted message is', encryptedString)
