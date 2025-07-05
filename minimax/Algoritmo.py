from copy import deepcopy
import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0) 

def minimax(posicion, prof, jugador_max, juego):
    if prof == 0 or posicion.ganador() != None:
        return posicion.evaluar(), posicion
    
    if jugador_max:
        maxEval = float('-inf')
        mejor_mov = None
        for mov in obtener_todos_movimientos(posicion, BLANCO, juego):
            evaluacion = minimax(mov, prof-1, False, juego)[0]
            maxEval = max(maxEval, evaluacion)
            if maxEval == evaluacion:
                mejor_mov = mov
        return maxEval, mejor_mov
    else:
        
        minEval = float('inf')
        mejor_mov = None
        for mov in obtener_todos_movimientos(posicion, NEGRO, juego):
            evaluacion = minimax(mov, prof-1, True, juego)[0]
            minEval = min(minEval, evaluacion)
            if minEval == evaluacion:
                mejor_mov = mov
        return minEval, mejor_mov
    
def simular_mov(pieza, mov, tablero, juego, salto):
    tablero.mover(pieza, mov[0], mov[1])
    if salto:
        tablero.eliminar(salto)

    return tablero