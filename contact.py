#CONTACT
import csv




first=input('first Name     ')

last=input('Last Name     ')

add=input('Address      ')

city=input('City      ')

state=input('State   ')

zip=input('Zip     ')

person = {'first':first,'last':last,'address':add, 'city':city,'state':state,'zip':zip}

print()
print(last+', '+first)        #Print to screen in business card format
print (add)     
print(city+', '+state+'  '+zip)
print()

print(person['last']+', ' + person['first'])
print (person['address'])
print(person['city']+','+person['state']+','+person['zip'])


answer = input('Correct, Y/N? ')
while answer !='y':
    for field in person:
        edit=input(person[field]+'  ')
        if edit!='':
            person[field]=edit
    answer = input('Correct, Y/N? ')       
        
          




#if: correct then save alphabetically using dictionary
#if not return to top
#Check for duplicate   
#ass anuther file?
     


               
               
    
