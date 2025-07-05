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