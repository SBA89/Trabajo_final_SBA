mi_diccionario = {}
matriz1 = [['🪑','🪑','🪑','🪑','🪑'],
           ['🪑','🪑','🪑','🪑','🪑'],
           ['🪑','🪑','🪑','🪑','🪑'],
           ['🪑','🪑','🪑','🪑','🪑'],
           ['🪑','🪑','🪑','🪑','🪑']]
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
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        mi_diccionario[name] = {'GENERO': genero, 'CANTIDAD': cantidad}
        enter = input('\n\nEl libro ha sido registrado.\n Presione ENTER para continuar...')   
        os.system('cls')   
    
        
def fnt_registro():
    fnt_limpiar()
    name = input('Ingrese nombre de la pelicula: ') 
    genero = input('Ingrese el genero de el libro: ')
    cantidad = input('Cantidad de entradas: ')
    fnt_agregar(mi_diccionario, name, genero, cantidad)
    
def fnt_buscar():
    fnt_limpiar()
    if buscar in mi_diccionario:
        print(mi_diccionario[buscar])
        enter = input('Presione <ENTER> para continuar')
    
        
    else:
        print('El libro no se encuentra registrado')
        enter = input('Presione <Enter> para continuar')
    os.system('cls')
    
    

while sw == True:   
    fnt_limpiar()
    print('<<< BIENVENIDO A LA BIBLIOTECA SBA >>>\n')
    print('Selecciones que acción deseas realizar\n')
    opcion = input('1. INGRESAR\n2. BUSCAR\n3. SALIR\n--> ')
    if opcion == '1':
        fnt_registro()
    if opcion == '2':
        buscar =input('Ingrese el nombre del libro:  ')
        fnt_buscar()
    if opcion == '3':
        sw = False