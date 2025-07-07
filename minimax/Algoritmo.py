from copy import deepcopy
from Damas.arbol import Nodo
import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)     

def minimax_nodo(nodo, prof, juego):
    if prof == 0 or nodo.estado.ganador() is not None:
        nodo.evaluacion = nodo.estado.evaluar()
        return nodo.evaluacion

    if nodo.turno_max:
        maxEval = float('-inf')
        for mov in obtener_todos_movimientos(nodo.estado, BLANCO, juego):
            hijo = Nodo(mov, turno_max=False, padre=nodo)
            nodo.agregar_hijo(hijo)
            evaluacion = minimax_nodo(hijo, prof-1, juego)
            if evaluacion > maxEval:
                maxEval = evaluacion
                nodo.evaluacion = maxEval
    else:
        minEval = float('inf')
        for mov in obtener_todos_movimientos(nodo.estado, NEGRO, juego):
            hijo = Nodo(mov, turno_max=True, padre=nodo)
            nodo.agregar_hijo(hijo)
            evaluacion = minimax_nodo(hijo, prof-1, juego)
            if evaluacion < minEval:
                minEval = evaluacion
                nodo.evaluacion = minEval

    return nodo.evaluacion


def simular_mov(pieza, mov, tablero, juego, salto):
    tablero.mover(pieza, mov[0], mov[1])
    if salto:
        tablero.eliminar(salto)

    return tablero

def obtener_todos_movimientos(tablero, color, juego):
    movimientos = []

    for pieza in tablero.obtener_todas_piezas(color):
        mov_valido = tablero.obtener_mov_validos(pieza)
        for mov, salto in mov_valido.items():
            
            tablero_temp = deepcopy(tablero)
            pieza_temp = tablero_temp.obtener_pieza(pieza.fila, pieza.columna)
            nuevo_tablero = simular_mov(pieza_temp, mov, tablero_temp, juego, salto)
            movimientos.append(nuevo_tablero)
    
    return movimientos

def dibujar_movimientos(juego, tablero, pieza):
    mov_validos = tablero.obtener_todos_movimientos(pieza)
    tablero.dibujar(juego.ventana)
    pygame.draw.circle(juego.ventana, (0,255,0), (pieza.x, pieza.y), 50, 5)
    juego.dibujar_mov_validos(mov_validos.keys())
    pygame.display.update()
    pygame.time.delay(5000)