# Hanoi program
# http://towersofhanoi.info/Tech.aspx

# Library import 
###################################################

import copy, sys, os, time

# Declaracion variables
###################################################

limpia_pantalla = 'clear' if os.name == 'posix' else 'CLS'
count = 0
discos = 0 #numero de discos
torres = 0
lista_torres = []
origen = 0
destino = 0
torres_intermedias = []
estado_inicial = []
estado_actual = []
estado_final = []
movimiento_actual = 0

# Declaracion de funciones
###################################################

def Peticion_variables():
    os.system(limpia_pantalla)
    print('================================================')
    print('Bienvenidos al juego de las Torres de Hanoi v0.2')
    print('================================================')
    print()
    global discos, torres, estado_actual, origen, destino, torres_intermedias, lista_torres
    while discos == 0 or not discos.isnumeric():
        discos = input('Introduce el número de discos : ')
    discos = int(discos)
    while torres == 0 or not torres.isnumeric():
        torres = input('Introduce el número de torres : ')
    torres = int(torres)
    lista_torres = [x for x in range(1,torres+1)]
    while origen == 0 or not origen.isnumeric():
        print('Introduce la torre origen ', [x for x in range(1,torres+1)] ,' : ')
        origen = input()
    origen = int(origen)
    while destino == 0 or not destino.isnumeric():
        x= [x for x in range(1,torres+1)]
        x.remove(origen)
        print('Introduce la torre destino',x,' : ')
        destino = input()
    destino = int(destino)
    torres_intermedias = [x for x in range(1,torres+1)]
    torres_intermedias.remove(origen)
    torres_intermedias.remove(destino)
    for x in range(torres):
        if x == origen-1:
            estado_inicial.append([x for x in range(1,discos+1)])
        else:
            estado_inicial.append([])
    estado_actual = copy.deepcopy(estado_inicial)
    for x in range(torres):
        if x == destino-1:
            estado_final.append([x for x in range(1,discos+1)])
        else:
            estado_final.append([])
    count = 3
    print('Empezando en :')
    for x in range(count,0, -1):
        print(x,'...')
        time.sleep(1)


def Print_state():
    os.system(limpia_pantalla)
    print('====================')
    print('Torres de Hanoi v0.2')
    print('====================')
    print()
    print('Discos : ',discos)
    print('Torres : ',torres)
    print('Torre de origen : ',origen)
    print('Torre de destino : ',destino)
    print('Torres intermedias : ',torres_intermedias)
    print('Estado inicial : ', estado_inicial)
    print('Estado actual :  ', estado_actual)
    print('Estado final :   ', estado_final)
    print('Movimiento actual : ', movimiento_actual)
    time.sleep(0.7)

def Mover_disco(origen,destino):
    global movimiento_actual
    estado_actual[destino-1].insert(0,estado_actual[origen-1][0])
    estado_actual[origen-1].pop(0)
    movimiento_actual += 1
    
def Comprueba_mov(origen,destino):
    if not estado_actual[destino-1] or estado_actual[destino-1][0] > estado_actual[origen-1][0]:
        return True
    else:
        return False

# def Algoritmo(discos , origen, destino, intermedios):
#     if discos==1:
#         if Comprueba_mov(origen,destino):
#             Mover_disco(origen,destino)
#             Print_state()
#             if estado_actual==estado_final:
#                 print('Terminado en ',movimiento_actual,' movimientos.')
#         return
#     Algoritmo(discos-1, origen, intermedios, destino)
#     if Comprueba_mov(origen,destino):
#         Mover_disco(origen,destino)
#         Print_state()
#     Algoritmo(discos-1, intermedios, destino, origen)
            
def Algoritmo(discos,origen,destino,torres_intermedias):
    for node in range(len(torres_intermedias)):
        d = torres_intermedias[0]
        via = d
        torres_intermedias.remove(d)
        torres_intermedias.append(destino)
        Algoritmo(discos,origen,d,torres_intermedias)
    if Comprueba_mov(origen,destino):
        Mover_disco(origen,destino)
        Print_state()
    for node in reversed(torres_intermedias):
        s = via
        torres_intermedias.append(destino)
        Algoritmo(discos,origen,d,torres_intermedias)
        torres_intermedias.append(s)


# >>> MAIN CODE >>>>
###################################################

Peticion_variables()
Print_state()
Algoritmo(discos,origen,destino, torres_intermedias)