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
torres = 3
estado_inicial = []
estado_actual = []
estado_final = []
movimiento_actual = 0
movimientos_prediccion = 0

# Declaracion de funciones
###################################################

def Peticion_variables():
    os.system(limpia_pantalla)
    print('================================================')
    print('Bienvenidos al juego de las Torres de Hanoi v0.1')
    print('================================================')
    print()
    global discos, torres, estado_actual, movimientos_prediccion
    while discos == 0 or not discos.isnumeric():
        discos = input('Introduce el número de discos : ')
    discos = int(discos)
    for x in range(torres):
        if x == 0:
            estado_inicial.append([x for x in range(1,discos+1)])
        else:
            estado_inicial.append([])
    estado_actual = copy.deepcopy(estado_inicial)
    for x in range(torres):
        if x == torres-1:
            estado_final.append([x for x in range(1,discos+1)])
        else:
            estado_final.append([])
    count = 3
    movimientos_prediccion = 2**discos-1
    print('Empezando en :')
    for x in range(count,0, -1):
        print(x,'...')
        time.sleep(1)


def Print_state():
    os.system(limpia_pantalla)
    print('====================')
    print('Torres de Hanoi v0.1')
    print('====================')
    print()
    print('Discos: ',discos)
    print('Torres: ',torres)
    print('Estado inicial : ', estado_inicial)
    print('Estado actual :  ', estado_actual)
    print('Estado final :   ', estado_final)
    print('Predicción de movimientos: ', movimientos_prediccion)
    print('Movimiento actual : ', movimiento_actual)
    time.sleep(0.7)

def Mover_disco(inicio,final):
    global movimiento_actual
    estado_actual[final-1].insert(0,estado_actual[inicio-1][0])
    estado_actual[inicio-1].pop(0)
    movimiento_actual += 1
    
def Comprueba_mov(inicio,final):
    if not estado_actual[final-1] or estado_actual[final-1][0] > estado_actual[inicio-1][0]:
        return True
    else:
        return False

def Algoritmo(discos , inicio, final, intermedios):
    if discos==1:
        if Comprueba_mov(inicio,final):
            Mover_disco(inicio,final)
            Print_state()
            if estado_actual==estado_final:
                print('Terminado en ',movimiento_actual,' movimientos.')
        return
    Algoritmo(discos-1, inicio, intermedios, final)
    if Comprueba_mov(inicio,final):
        Mover_disco(inicio,final)
        Print_state()
    Algoritmo(discos-1, intermedios, final, inicio)


# >>> MAIN CODE >>>>
###################################################

Peticion_variables()
Print_state()
Algoritmo(discos,1,torres,torres-1)