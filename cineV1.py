# Este algoritmo permite crear salas para un teatro
# las salas son ajustables, se les permite ingresar la cantidad de columnas y filas 
# Se permite ingresar nombre del show que se llevara acabo en la sala y precio de la boleta
# se permite ver las salas y asientos ocupados(si el asiento lleva un 00 ya no se encuentra disponible) 

import os
salas=[]
info_salas=[]
def crearsala():
    sala=[]
    info=[]
    nombre=input('Ingrese nombre de la sala: ')
    precio=input('Ingrese precio de boleta de la sala: ')
    filas=int(input('ingrese numero de filas: '))
    columnas=int(input('ingrese numero de columnas: '))
    info.append(nombre)
    info.append(precio)
    info_salas.append(info)
    numsilla=0
    for i in range(columnas):
        sillas=[]
        for j in range(filas):
            numsilla+=1
            sillas.append(numsilla)
        sala.append(sillas)
    salas.append(sala)
    input('Sala creada con exito presione ENTER')

def versalas():
    for i in range(len(salas)):
        print('=== INFO SALAS ===')
        print(f'Nombre de la sala: {info_salas[i][0]}')
        print(f'Precio boleta de la sala: {info_salas[i][1]}')
        for j in range(len(salas[i])):
            for k in range(len(salas[i])):
                print(f'{salas[i][j][k]:02}',end=' ')
            print('')

def venderboleta():
    print('=== SALAS DISPONIBLES ===')
    for i in range(len(info_salas)):
        print(f'Sala {i+1}: {info_salas[i][0]}')
        print(f'precio boleta: ${info_salas[i][1]}')  
    sala_ver= int(input('ingrese numero de sala que desea ver: '))
    
    print(f'=== SALA {info_salas[sala_ver-1][0]} ===')
    for i in range(len(salas[sala_ver-1])):
        print(salas[sala_ver-1][i])    
    print('SI LA SILLA CUENTA CON 0 ESTA OCUPADA')  
    silla=int(input('Elija su silla: '))
    
    for i in range(len(salas[sala_ver-1])):
        if silla in salas[sala_ver-1][i]:
            index = salas[sala_ver-1][i].index(silla)
            salas[sala_ver-1][i][index] = 0
            print('Silla reservada con éxito.')
            break
              
       
def menu_principal():
    opc=1
    while(opc!=0):
        print('==== TEATRO ===')
        print('1. Crear sala')
        print('2. Ver salas')
        print('3. Vender boleto')
        print('4. Cargar sala')
        opc=int(input('Ingrese una opcion: '))
        if(opc==1):
            crearsala()
        if(opc==2):
            versalas()
        if(opc==3):
            venderboleta()
        if(opc==4):
            versalas()
            
       
os.system('cls')
menu_principal() 