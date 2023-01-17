
# Library import 
###################################################

import copy, sys, os, time

# Declaracion variables
###################################################

limpia_pantalla = 'clear' if os.name == 'posix' else 'CLS'
discos = 0
torres = 0
origen = 0
destino = 0
estado_inicial = []
estado_actual = []
estado_final = []
movimientos_prediccion = 0
movimiento_actual = 0
speed = 0

abiertos=[estado_inicial]
cerrados=[]

################################################################

def Reset():
    global discos,torres, origen, destino, estado_inicial,estado_actual,estado_final,movimientos_prediccion,movimiento_actual,speed,abiertos,cerrados
    
    discos = 0
    torres = 0
    origen = 0
    destino = 0
    estado_inicial = []
    estado_actual = []
    estado_final = []
    movimientos_prediccion = 0
    movimiento_actual = 0
    speed = 0
    abiertos=[estado_inicial]
    cerrados=[]

def Peticion_variables():
    os.system(limpia_pantalla)
    print('================================================')
    print('Bienvenidos al juego de las Torres de Hanoi v0.2')
    print('================================================')
    print()
    global discos, torres, estado_actual, origen, destino, torres_intermedias, lista_torres, movimientos_prediccion,speed
    while discos == 0 or not discos.isnumeric():
        discos = input('Introduce el número de discos (No más de 6): ')
    discos = int(discos)
    while torres == 0 or not torres.isnumeric():
        torres = input('Introduce el número de torres (No más de 6): ')
    torres = int(torres)
    lista_torres = [x for x in range(1,torres+1)]
    while origen == 0 or not origen.isnumeric():
        print('Introduce la torre origen ', [x for x in range(1,torres+1)] ,' : ', end='')
        origen = input()
    origen = int(origen)
    while destino == 0 or not destino.isnumeric():
        x= [x for x in range(1,torres+1)]
        x.remove(origen)
        print('Introduce la torre destino',x,' : ', end='')
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
    movimientos_prediccion = 2**discos-1
    while speed == 0 or not speed.isnumeric():
        print('Introduce la velocidad (recomendado de 1 a 20) : ', end='')
        speed = input()
    speed = float(speed)
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
    if torres  == 3:
        print('Movimientos mínimos: ', movimientos_prediccion)
    print('Movimiento actual : ', movimiento_actual)
    time.sleep(1/speed)

def Comprueba_estado(state):
    assert type(state)== list and len(state)==torres
    def es_valido(t):
        for n in range(len(t)-1):
            if(t[n]>t[n+1]):
                return False
        return True
    def comprueba_torres(s):
        for x in range(len(s)):
            if not es_valido(s[x]):
                return False
        return True
    if comprueba_torres(state):
        return True
    else:
        return False

def estados(s):
    for del_torre in range(len(s)):
        for add_torre in range(len(s)):
            ns=copy.deepcopy(s)
            if add_torre != del_torre and ns[del_torre]:
                ns[add_torre].insert(0,ns[del_torre][0])
                ns[del_torre].pop(0)
                yield ns

def Profundidad(actual, path=[]):
    if actual==estado_final:
        return [actual]
    else: 
        for ns in estados(actual):
            if Comprueba_estado(ns) and ns not in cerrados:
                cerrados.append(ns)
                r=Profundidad(ns,cerrados)
                if r:
                    r.insert(0,actual)
                    return r
        return []

def Pedir_listado():
    listado = input('===========================================\n¿Quiere mostrar el listado de los pasos?\n[S]i  para listarlo a continuación : ').upper()
    if listado == 'S':
        print('\nAquí tiene la solución, paso a paso\n')
        for paso in solucion:
            print(paso)
        print('\nGracias por usar el programa "Torres de Hanoi v0.1"\n')
    else:
        print('\nGracias por usar el programa "Torres de Hanoi v0.1"\n')

def Ejecucion_total():
    global estado_actual,movimiento_actual
    Reset()
    try:
        Peticion_variables()
        solucion = Profundidad(estado_inicial)
        Print_state()
        for paso in solucion:
            estado_actual = paso
            Print_state()
            movimiento_actual += 1
        Pedir_listado()
    except RecursionError:
        print('Disculpe las molestias pero con los parámetros introducimos, se excede la capacidad de cómputo del intérprete.\nPor favor, vuelva a introducir nuevos parámetros con valores más bajos de Discos y/o Torres.')
        input('Pulse cualquier tecla para continuar...')
        Ejecucion_total()

# MAIN CODE ####################################################
################################################################
    
Ejecucion_total()
