#trans



alienDictionary = {'we': 'vorag', 'come': 'thang', 'in': 'zon', 'peace': 'arga', 'hello': 'kodar', 'can': 'znak', 'i': 'az', 'borrow': 'lifit', 'some': 'zum', 'rocket': 'upgoman',
                   'fuel': 'kakboom', 'please': 'zelpin', 'dont': 'baaaaaaaaarn', 'shoot': 'flabil', 'welcome': 'unkip', 'our': 'mandig', 'now': 'brang', 'alien': 'marangan', 'overlords': 'bap'}

englishPhrase = input('Please enter an english worr or phrase to translate: ')
englishWords = englishPhrase.lower().split()

alienWords = []
for word in englishWords:
    if word in alienDictionary:
       alienWords.append(alienDictionary[word])
    else:
        alienWords.append(word)
print('in alien, say: ',' '.join(alienWords))        

