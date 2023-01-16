
# Library import 
###################################################

import copy, sys, os, time

# Declaracion variables
###################################################

# limpia_pantalla = 'clear' if os.name == 'posix' else 'CLS'
discos = 4
torres = 3
lista_torres = []
origen = 1
destino = 3
torres_intermedias = []
estado_inicial = [[1,2,3],[],[]]
estado_actual = [[1,2,3],[],[]]
estado_final = [[],[],[1,2,3]]
movimiento_actual = 0

abiertos=[estado_inicial]
cerrados=[]

################################################################

def Comprueba_estado(state):
    for state in estado_actual:
        x=copy.deepcopy(state)
        x.sort()
        # print(state)
        # print(x)
        if (state and state==x) or not state:
            pass
        else:
            return False
    return True

def states(s):
    # assert type(s)== list and len(s)==2
    # assert type(s[0]) == set

    for c in len(s):
        ns=copy.deepcopy(s)
        ns[0]=ns
        ns[1]=ns[lp].difference({"P",c})
        ns[2]=ns[lp].difference({"P",c})
        yield ns

def búsquedaProfundidadPlus(actual, path=[]):
    #En una función recursiva es importante saber que casos no son posibles
    if actual==estado_final:
        yield path + [actual]

    else:
        path.append(actual)#se añade a si misma a la derecha
        for ns in states(actual):#se van generando los hijos de actual
            if Comprueba_estado(ns) and ns not in path:#si es valido el estado (el hijo) y no se genera un ciclo 
                yield from búsquedaProfundidadPlus(ns,path)#preguntar que hace
        path.pop()

################################################################

for solución in búsquedaProfundidadPlus(estado_inicial):
    print('Solución : ')
    print(solución)