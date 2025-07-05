import pygame
from .const import NEGRO, BLANCO, CELESTE, TAM_CASILLERO
from Damas.tablero import Tablero

class Juego:
    def __init__(self, ventana):
        self._init()
        self.ventana = ventana
    
    def actualizar(self):
        self.tablero.dibujar(self.ventana)
        self.dibujar_mov_validos(self.mov_validos)
        pygame.display.update()

    def _init(self):
        self.seleccionado = None
        self.tablero = Tablero()
        self.turno = NEGRO
        self.mov_validos = {}

    def ganador(self):
        return self.tablero.ganador()

    def reiniciar(self):
        self._init()

    def seleccionar(self, fila, columna):
        if self.seleccionado:
            resultado = self._mover(fila, columna)
            if not resultado:
                self.seleccionado = None
                self.seleccionar(fila, columna)
        
        pieza = self.tablero.obtener_pieza(fila, columna)
        if pieza != 0 and pieza.color == self.turno:
            self.seleccionado = pieza
            self.mov_validos = self.tablero.obtener_mov_validos(pieza)
            return True
            
        return False

    def _mover(self, fila, columna):
        pieza = self.tablero.obtener_pieza(fila, columna)
        if self.seleccionado and pieza == 0 and (fila, columna) in self.mov_validos:
            self.tablero.mover(self.seleccionado, fila, columna)
            fichas_comidas = self.mov_validos[(fila, columna)]
            if fichas_comidas:
                self.tablero.eliminar(fichas_comidas)
            self.cambiar_turno()
        else:
            return False

        return True

    def dibujar_mov_validos(self, movimientos):
        for mov in movimientos:
            fila, columna = mov
            pygame.draw.circle(self.ventana, CELESTE, (columna * TAM_CASILLERO + TAM_CASILLERO//2, fila * TAM_CASILLERO + TAM_CASILLERO//2), 15)

    def cambiar_turno(self):
        self.mov_validos = {}
        if self.turno == NEGRO:
            self.turno = BLANCO
        else:
            self.turno = NEGRO

    def obtener_tablero(self):
        return self.tablero

    def mov_ia(self, tablero):
        self.tablero = tablero
        self.cambiar_turno()