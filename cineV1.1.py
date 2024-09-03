# Este algoritmo permite crear salas para un teatro
# las salas son ajustables, se les permite ingresar la cantidad de columnas y filas 
# Se permite ingresar nombre del show que se llevara acabo en la sala y precio de la boleta
# Se permite ver las salas y asientos ocupados (si el asiento lleva un 00 ya no se encuentra disponible) 
# Versión 1.1 
# Se le agregó leer y escribir archivo txt para guardar la sala

import os  # Importa el módulo os para interactuar con el sistema operativo
salas = []  # Lista que almacenará las salas creadas
info_salas = []  # Lista que almacenará la información de las salas (nombre, precio)

def crearsala():
    sala = []  # Lista para almacenar la disposición de asientos de la sala
    info = []  # Lista para almacenar el nombre y precio de la sala
    nombre = input('Ingrese nombre de la sala: ')  # Solicita el nombre de la sala al usuario
    precio = input('Ingrese precio de boleta de la sala: ')  # Solicita el precio del boleto
    filas = int(input('Ingrese número de filas: '))  # Solicita el número de filas en la sala
    columnas = int(input('Ingrese número de columnas: '))  # Solicita el número de columnas en la sala
    info.append(nombre)  # Añade el nombre de la sala a la lista info
    info.append(precio)  # Añade el precio de la sala a la lista info
    info_salas.append(info)  # Añade la información de la sala a la lista general info_salas
    numsilla = 0  # Inicializa el contador de número de sillas
    
    # Crea la disposición de asientos de la sala en base a filas y columnas
    for i in range(columnas):
        sillas = []  # Lista para almacenar las sillas en una columna
        for j in range(filas):
            numsilla += 1  # Incrementa el número de silla
            sillas.append(numsilla)  # Añade el número de silla a la columna
        sala.append(sillas)  # Añade la columna de sillas a la sala
    salas.append(sala)  # Añade la sala a la lista general de salas
    guardarsalatxt(salas, nombre, precio)  # Guarda la sala en un archivo de texto
    input('Sala creada con éxito, presione ENTER')  # Mensaje de éxito
    return salas  # Retorna la lista de salas


def guardarsalatxt(salas, nombre, precio):
    # Abre (o crea) un archivo de texto para guardar la sala, en modo escritura
    archivosala = open('Proyecto_Teatro\\Teatrosala.txt', mode='w', encoding='utf-8')
    for i in range(len(salas)):  # Itera sobre cada sala
        archivosala.write(f'\n==== {nombre} ====\n')  # Escribe el nombre de la sala en el archivo
        archivosala.write(f'=== precio: ${precio} ===\n')  # Escribe el precio de la sala en el archivo
        for j in range(len(salas[i])):  # Itera sobre cada columna de la sala
            for k in range(len(salas[i][j])):  # Itera sobre cada fila de la columna
                archivosala.write(f' {salas[i][j][k]:02} ')  # Escribe el número de silla en el archivo
            archivosala.write(f'\n')  # Salta a la siguiente línea para la siguiente columna
    archivosala.write(f'\n')  # Salta a la siguiente línea
    archivosala.close()  # Cierra el archivo


def cargarsalas():
    for i in range(len(salas)):  # Itera sobre cada sala creada
        print('=== INFO SALAS ===')
        print(f'Nombre de la sala: {info_salas[i][0]}')  # Muestra el nombre de la sala
        print(f'Precio boleta de la sala: {info_salas[i][1]}')  # Muestra el precio del boleto
        for j in range(len(salas[i])):  # Itera sobre cada columna de la sala
            for k in range(len(salas[i])):  # Itera sobre cada fila de la columna
                print(f'{salas[i][j][k]:02}', end=' ')  # Imprime el número de silla en formato 2 dígitos
            print('')  # Salta a la siguiente línea después de cada columna


def venderboleta():
    print('=== SALAS DISPONIBLES ===')
    for i in range(len(info_salas)):  # Itera sobre la información de cada sala
        print(f'Sala {i+1}: {info_salas[i][0]}')  # Muestra el número y nombre de la sala
        print(f'Precio boleta: ${info_salas[i][1]}')  # Muestra el precio del boleto
    sala_ver = int(input('Ingrese número de sala que desea ver: '))  # Solicita al usuario seleccionar una sala
    
    print(f'=== SALA {info_salas[sala_ver-1][0]} ===')  # Muestra el nombre de la sala seleccionada
    for i in range(len(salas[sala_ver-1])):  # Itera sobre las filas de la sala seleccionada
        print(salas[sala_ver-1][i])  # Muestra la disposición de sillas
    print('SI LA SILLA CUENTA CON 0 ESTA OCUPADA')  # Indica que un asiento con 0 está ocupado
    silla = int(input('Elija su silla: '))  # Solicita al usuario elegir una silla
    
    for i in range(len(salas[sala_ver-1])):  # Itera sobre las filas de la sala seleccionada
        if silla in salas[sala_ver-1][i]:  # Verifica si la silla seleccionada está disponible
            index = salas[sala_ver-1][i].index(silla)  # Encuentra el índice de la silla en la fila
            salas[sala_ver-1][i][index] = 0  # Marca la silla como ocupada (0)
            print('Silla reservada con éxito.')  # Muestra mensaje de éxito
            break  # Termina el ciclo después de reservar la silla


def versalas():
    # Abre el archivo de texto que contiene las salas en modo lectura
    archivo = open('Proyecto_Teatro\\Teatrosala.txt', mode='r', encoding='utf-8')
    sala = archivo.read()  # Lee el contenido del archivo
    print(sala)  # Muestra el contenido de las salas en la consola
    archivo.close()  # Cierra el archivo


def menu_principal():
    opc = 1  # Inicializa la opción seleccionada en el menú principal
    while(opc != 0):  # Bucle para mostrar el menú mientras no se seleccione la opción de salida (0)
        print('==== TEATRO ===')
        print('1. Crear sala')
        print('2. Ver salas')
        print('3. Vender boleto')
        print('4. Cargar sala')
        opc = int(input('Ingrese una opción: '))  # Solicita al usuario seleccionar una opción
        if(opc == 1):  # Si la opción es 1, crea una sala
            crearsala()
        if(opc == 2):  # Si la opción es 2, muestra las salas guardadas
            versalas()
        if(opc == 3):  # Si la opción es 3, permite vender una boleta
            venderboleta()
        if(opc == 4):  # Si la opción es 4, carga las salas en memoria y las muestra
            cargarsalas()

os.system('cls')  # Limpia la consola
menu_principal()  # Llama al menú principal para iniciar la interacción con el usuario