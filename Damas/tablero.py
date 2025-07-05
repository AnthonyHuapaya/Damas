import pygame
from .const import MARRON, FILAS, NEGRO, TAM_CASILLERO, COLUMNAS, BLANCO, NARANJA, COLOR_PANEL, ANCHO_P, ALTO_P, ANCHO_P_VENTANA, COLOR_TEXTO, FUENTE_TEXTO, TITULO_PANEL, FUENTE_TITULO, BOTON_BACK
from .pieza import Pieza

class Tablero:
    def __init__(self):
        self.tablero = []
        self.cant_negros = self.cant_blancos = 12
        self.reinas_negras = self.reinas_blancas = 0
        self.crear_tablero()
    
    def dibujar_casillas(self, ventana):
        ventana.fill(MARRON)
        for fila in range(FILAS):
            for columna in range(fila % 2, COLUMNAS, 2):
                pygame.draw.rect(ventana, NARANJA, (fila*TAM_CASILLERO, columna *TAM_CASILLERO, TAM_CASILLERO, TAM_CASILLERO))

    def dibujar_panel(self, ventana):
        PADDING = 15
        OUTLINE = 2
        pygame.draw.rect(ventana, COLOR_PANEL, (ANCHO_P, 0, ANCHO_P_VENTANA - ANCHO_P, ALTO_P))
        pygame.draw.rect(ventana, BLANCO, (ANCHO_P, 360, ANCHO_P_VENTANA - ANCHO_P, 5))

        #Informacion general
        ventana.blit(TITULO_PANEL, (ANCHO_P + 40, 20))  

        #Boton exit
        ventana.blit(BOTON_BACK, (ANCHO_P + 40, 630))

        #Informacion fichas negras
        text_negro_titulo = FUENTE_TITULO.render(f"FICHA:", True, COLOR_TEXTO)
        radio = TAM_CASILLERO//2 - PADDING
        pygame.draw.circle(ventana, NARANJA, (ANCHO_P + 200, 150), radio + OUTLINE)
        pygame.draw.circle(ventana, NEGRO, (ANCHO_P + 200, 150), radio)
        texto_negro_fichas_totales = FUENTE_TEXTO.render(f"Fichas totales: {self.cant_negros}", True, COLOR_TEXTO)
        texto_negro_fichas_ganadas = FUENTE_TEXTO.render(f"Fichas ganadas: {12 - self.cant_blancos}", True, COLOR_TEXTO)
        texto_negro_reinas_totales = FUENTE_TEXTO.render(f"Reinas: {self.reinas_negras}", True, COLOR_TEXTO)
        ventana.blit(text_negro_titulo, (ANCHO_P + 20, 130))
        ventana.blit(texto_negro_fichas_totales, (ANCHO_P + 20, 190))
        ventana.blit(texto_negro_fichas_ganadas, (ANCHO_P + 20, 220))
        ventana.blit(texto_negro_reinas_totales, (ANCHO_P + 20, 250))

        #Informacion fichas blancas
        text_blanca_titulo = FUENTE_TITULO.render(f"FICHA:", True, COLOR_TEXTO)
        radio = TAM_CASILLERO//2 - PADDING
        pygame.draw.circle(ventana, NARANJA, (ANCHO_P + 200, 460), radio + OUTLINE)
        pygame.draw.circle(ventana, BLANCO, (ANCHO_P + 200, 460), radio)
        texto_blanca_fichas_totales = FUENTE_TEXTO.render(f"Fichas totales: {self.cant_blancos}", True, COLOR_TEXTO)
        texto_blanca_fichas_ganadas = FUENTE_TEXTO.render(f"Fichas ganadas: {12 - self.cant_negros}", True, COLOR_TEXTO)
        texto_blanca_reinas_totales = FUENTE_TEXTO.render(f"Reinas: {self.reinas_blancas}", True, COLOR_TEXTO)
        ventana.blit(text_blanca_titulo, (ANCHO_P + 20, 440))
        ventana.blit(texto_blanca_fichas_totales, (ANCHO_P + 20, 500))
        ventana.blit(texto_blanca_fichas_ganadas, (ANCHO_P + 20, 530))
        ventana.blit(texto_blanca_reinas_totales, (ANCHO_P + 20, 560))


    #Evalua el puntaje
    def evaluar(self):
        return self.cant_blancos - self.cant_negros + (self.reinas_blancas * 0.5 - self.reinas_negras * 0.5)

    #Obtención de todas las piezas
    def obtener_todas_piezas(self, color):
        piezas = []
        for fila in self.tablero:
            for pieza in fila:
                if pieza != 0 and pieza.color == color:
                    piezas.append(pieza)
        return piezas

    #Movimiento
    def mover(self, pieza, fila, columna):
        self.tablero[pieza.fila][pieza.columna], self.tablero[fila][columna] = self.tablero[fila][columna], self.tablero[pieza.fila][pieza.columna]
        pieza.mover(fila, columna)

        if fila == FILAS - 1 or fila == 0:
            # pieza.conv_reina()
            # if pieza.color == BLANCO:
            #     self.reinas_blancas += 1
            # else:
            #     self.reinas_negras += 1 

            if pieza.conv_reina():
                if pieza.color == BLANCO:
                    self.reinas_blancas += 1
                else:
                    self.reinas_negras += 1 


    def obtener_pieza(self, fila, columna):
        return self.tablero[fila][columna]

    def crear_tablero(self):
        for fila in range(FILAS):
            self.tablero.append([])
            for columna in range(COLUMNAS):
                if columna % 2 == ((fila +  1) % 2):
                    if fila < 3:
                        self.tablero[fila].append(Pieza(fila, columna, BLANCO))
                    elif fila > 4:
                        self.tablero[fila].append(Pieza(fila, columna, NEGRO))
                    else:
                        self.tablero[fila].append(0)
                else:
                    self.tablero[fila].append(0)
        
    def dibujar(self, ventana):
        self.dibujar_casillas(ventana)
        self.dibujar_panel(ventana)
        for fila in range(FILAS):
            for columna in range(COLUMNAS):
                pieza = self.tablero[fila][columna]
                if pieza != 0:
                    pieza.dibujar(ventana)

    def eliminar(self, piezas):
        for pieza in piezas:
            self.tablero[pieza.fila][pieza.columna] = 0
            if pieza != 0:
                if pieza.color == NEGRO:
                    if pieza.reina: self.reinas_negras -= 1
                    self.cant_negros -= 1
                else:
                    if pieza.reina: self.reinas_blancas -= 1
                    self.cant_blancos -= 1
    
    def ganador(self):
        if self.cant_negros <= 0:
            return BLANCO
        elif self.cant_blancos <= 0:
            return NEGRO
        
        return None 
    
    def obtener_mov_validos(self, pieza):
        movimientos = {}
        izq = pieza.columna - 1
        der = pieza.columna + 1
        fila = pieza.fila

        if pieza.color == NEGRO or pieza.reina:
            movimientos.update(self._mov_validos_izquierda(fila -1, max(fila-3, -1), -1, pieza.color, izq))
            movimientos.update(self._mov_validos_derecha(fila -1, max(fila-3, -1), -1, pieza.color, der))
        if pieza.color == BLANCO or pieza.reina:
            movimientos.update(self._mov_validos_izquierda(fila +1, min(fila+3, FILAS), 1, pieza.color, izq))
            movimientos.update(self._mov_validos_derecha(fila +1, min(fila+3, FILAS), 1, pieza.color, der))
    
        return movimientos

    def _mov_validos_izquierda(self, inicio, stop, paso, color, izq, fichas_comidas=[]):
        movimientos = {}
        ultimo = []
        for r in range(inicio, stop, paso):
            if izq < 0:
                break
            
            current = self.tablero[r][izq]
            if current == 0:
                if fichas_comidas and not ultimo:
                    break
                elif fichas_comidas:
                    movimientos[(r, izq)] = ultimo + fichas_comidas
                else:
                    movimientos[(r, izq)] = ultimo
                
                if ultimo:
                    if paso == -1:
                        fila = max(r-3, 0)
                    else:
                        fila = min(r+3, FILAS)
                    movimientos.update(self._mov_validos_izquierda(r+paso, fila, paso, color, izq-1,fichas_comidas=ultimo))
                    movimientos.update(self._mov_validos_derecha(r+paso, fila, paso, color, izq+1,fichas_comidas=ultimo))
                break
            elif current.color == color:
                break
            else:
                ultimo = [current]

            izq -= 1
        
        return movimientos

    def _mov_validos_derecha(self, inicio, stop, paso, color, der, fichas_comidas=[]):
        movimientos = {}
        ultimo = []
        for r in range(inicio, stop, paso):
            if der >= COLUMNAS:
                break
            
            current = self.tablero[r][der]
            if current == 0:
                if fichas_comidas and not ultimo:
                    break
                elif fichas_comidas:
                    movimientos[(r,der)] = ultimo + fichas_comidas
                else:
                    movimientos[(r, der)] = ultimo
                
                if ultimo:
                    if paso == -1:
                        fila = max(r-3, 0)
                    else:
                        fila = min(r+3, FILAS)
                    movimientos.update(self._mov_validos_izquierda(r+paso, fila, paso, color, der-1,fichas_comidas=ultimo))
                    movimientos.update(self._mov_validos_derecha(r+paso, fila, paso, color, der+1,fichas_comidas=ultimo))
                break
            elif current.color == color:
                break
            else:
                ultimo = [current]

            der += 1
        
        return movimientos
