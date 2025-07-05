from .const import NEGRO, BLANCO, TAM_CASILLERO, NARANJA, CORONA
import pygame

class Pieza:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, fila, columna, color):
        self.fila = fila
        self.columna = columna
        self.color = color
        self.reina = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    #Calcular posicion
    def calc_pos(self):
        self.x = TAM_CASILLERO * self.columna + TAM_CASILLERO // 2
        self.y = TAM_CASILLERO * self.fila + TAM_CASILLERO // 2

    #Convertir a reina
    def conv_reina(self):
        if self.reina == True: return False
        else: 
            self.reina = True
            return True
        # self.reina = True
    
    #Dibujo de la ficha al tablero
    def dibujar(self, ventana):
        radio = TAM_CASILLERO//2 - self.PADDING
        pygame.draw.circle(ventana, NARANJA, (self.x, self.y), radio + self.OUTLINE)
        pygame.draw.circle(ventana, self.color, (self.x, self.y), radio)
        if self.reina:
            ventana.blit(CORONA, (self.x - CORONA.get_width()//2, self.y - CORONA.get_height()//2))

    #Mover la ficha
    def mover(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.calc_pos()

    def __repr__(self):
        return str(self.color)