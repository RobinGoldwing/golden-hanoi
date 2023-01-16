# Hanoi program

# Library import 
###################################################

import copy, sys, os, time

# Declaracion variables
###################################################

limpia_pantalla = 'clear' if os.name == 'posix' else 'CLS'
count = 0
discos = 0 #numero de discos
torres = 0 #numero de torres
estado_inicial = []
estado_actual = []
estado_final = []
auxiliares = []
# movimientos_prediccion = 0
movimiento_actual = 0

# Declaracion de funciones
###################################################

def Peticion_variables():
    os.system(limpia_pantalla)
    print('================================================')
    print('Bienvenidos al juego de las Torres de Hanoi v0.1')
    print('================================================')
    print()
    global auxiliares,discos, torres, estado_inicial, estado_actual, estado_final #, movimientos_prediccion
    while discos == 0 or not discos.isnumeric():
        discos = input('Introduce el número de discos : ')
    while torres == 0 or not torres.isnumeric() or int(torres) <= 2:
        torres = input('Introduce el número de torres (mínimno 3): ')
    discos = int(discos)
    torres = int(torres)
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
    # movimientos_prediccion = 1*2**0 + (torres-2)*2**1 + (discos-(1+(torres-2)))*2**2  + (discos-(2+(torres-2)))*2**3
    auxiliares = [x for x in range(2, torres)]
    count = 3
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
    # print('Predicción de número de movimientos : ', movimientos_prediccion)
    print('Movimiento actual : ', movimiento_actual)
    print('Torres auxiliares : ',auxiliares)

def hanoi(discos, inicio, final, auxiliares, torres):
    global movimiento_actual
    if discos > 0:
        # Move n-1 discs from inicio to auxiliary pegs
        hanoi(discos-1, inicio, auxiliares[0], auxiliares[1:], torres)
        # Move the n-th disc from inicio to final peg
        print("Move disk", discos, "from", inicio, "to", final)
        estado_actual[final].insert(0,estado_actual[inicio-1][0])
        estado_actual[inicio-1].pop(0)
        movimiento_actual += 1
        Print_state()
        time.sleep(0.7)
        # Move n-1 discs from auxiliary to final pegs
        hanoi(discos-1, auxiliares[0], final, inicio, torres)

Peticion_variables()
Print_state()
time.sleep(0.7)

hanoi(discos,1,torres-1,auxiliares,torres)