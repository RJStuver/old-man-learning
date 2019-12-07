#Spacelist

spacelist = ['rocket', 'planet', 'asteroid', 'alien']

spacelist[0] = 'planet Zarg'
del spacelist[0]
spacelist.append('moon')

for item in spacelist:
    print(item)
    
