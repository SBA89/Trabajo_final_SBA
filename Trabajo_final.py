dictionary = {}  
import os
sw = True
os.system('cls')        
def fnt_clean():
    import os
    os.system('cls')
    print('      |FINAL WORK|')
    print('Author: Santiago Barrera Arias')
    print('Date: April 21, 2024\n\n')
    

def fnt_add(dictionary, name, gender, amount):
    if name == '' or gender == '' or amount == '':
        enter = input('You must fill out all the requested information <ENTER>')
    else:
        dictionary[name] = {'Movie name': name,'Gender': gender, 'Number of tickets': amount}
        enter = input('\n\nTicket purchased successfully.\n Press <Enter> to continue...')   
        os.system('cls')   
    
        
def fnt_record():
    fnt_clean()
    name = input('Enter movie name: ') 
    gender = input('Enter the genre of the movie: ')
    amount = input('Number of tickets: ')
    fnt_add(dictionary, name, gender, amount)
    
def fnt_buscar():
    fnt_clean()
    if buscar in dictionary:
        print(dictionary[buscar])
        enter = input('Press <Enter> to continue')
    
        
    else:
        print('The film is not at the box office')
        enter = input('Press <Enter> to continue')
    os.system('cls')
    
    

while sw == True:   
    fnt_clean()
    print('<<< WELCOME TO THE CINEMA SBA >>>\n')
    print('Select what action you want to perform\n')
    opcion = input('1. BUY TICKETS\n2. LOOK FOR\n3. EXIT\n--> ')
    if opcion == '1':
        fnt_record()
    if opcion == '2':
        buscar =input('ENTER THE NAME OF THE MOVIE:  ')
        fnt_buscar()
    if opcion == '3':
        print('Program completed\nCome back...😈')
        sw = False