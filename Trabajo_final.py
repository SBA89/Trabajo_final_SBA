mi_diccionario = {}  
import os
sw = True
os.system('cls')        
def fnt_limpiar():
    import os
    os.system('cls')
    print('      |FINAL WORK|')
    print('Author: Santiago Barrera Arias')
    print('Date: April 21, 2024\n\n')
    

def fnt_agregar(mi_diccionario, name, genero, cantidad):
    if name == '' or genero == '' or cantidad == '':
        enter = input('You must fill out all the requested information <ENTER>')
    else:
        mi_diccionario[name] = {'Movie name': name,'Gender': genero, 'Number of tickets': cantidad}
        enter = input('\n\nTicket purchased successfully.\n Press <Enter> to continue...')   
        os.system('cls')   
    
        
def fnt_registro():
    fnt_limpiar()
    name = input('Enter movie name: ') 
    genero = input('Enter the genre of the movie: ')
    cantidad = input('Number of tickets: ')
    fnt_agregar(mi_diccionario, name, genero, cantidad)
    
def fnt_buscar():
    fnt_limpiar()
    if buscar in mi_diccionario:
        print(mi_diccionario[buscar])
        enter = input('Press <Enter> to continue')
    
        
    else:
        print('The film is not at the box office')
        enter = input('Press <Enter> to continue')
    os.system('cls')
    
    

while sw == True:   
    fnt_limpiar()
    print('<<< WELCOME TO THE CINEMA SBA >>>\n')
    print('Select what action you want to perform\n')
    opcion = input('1. BUY TICKETS\n2. LOOK FOR\n3. EXIT\n--> ')
    if opcion == '1':
        fnt_registro()
    if opcion == '2':
        buscar =input('ENTER THE NAME OF THE MOVIE:  ')
        fnt_buscar()
    if opcion == '3':
        print('Program completed\nCome back...😈')
        sw = False