import pygame
from Damas.const import ANCHO_P_VENTANA, ALTO_P_VENTANA, TAM_CASILLERO, NEGRO, BLANCO, FUENTE_PANTALLA_PRINCIPAL, FONDO_PANTALLA, ANCHO_P, FONDO_PANTALLA_WINNER, FONDO_PANTALLA_GAME_OVER
from Damas.juego import Juego
from Damas.boton import Boton
from Damas.arbol import Nodo
from Damas.arbol import Arbol
from minimax.Algoritmo import minimax_nodo

FPS = 60

VENTANA = pygame.display.set_mode((ANCHO_P_VENTANA, ALTO_P_VENTANA))
pygame.display.set_caption('DAMAS')

def obtener_fila_columna_mouse(pos):
    x, y = pos
    fila = y // TAM_CASILLERO
    columna = x // TAM_CASILLERO
    return fila, columna

def pantalla_inicio(juego_iniciado):
    texto = FUENTE_PANTALLA_PRINCIPAL.render("DAMAS", True, BLANCO)
    rect_texto = texto.get_rect(center=(ANCHO_P_VENTANA // 2, 150))

    def boton_play_evento():
        juego_iniciado[0] = True

    boton_play = Boton("assets/play_button.png", (ANCHO_P_VENTANA // 2, 510), boton_play_evento)

    def boton_exit_evento():
        pygame.quit()
        exit()

    boton_exit = Boton("assets/exit_button.png", (ANCHO_P_VENTANA // 2, 620), boton_exit_evento)

    while not juego_iniciado[0]:
        VENTANA.blit(FONDO_PANTALLA, (0, 0))
        VENTANA.blit(texto, rect_texto)
        boton_play.dibujar(VENTANA)
        boton_exit.dibujar(VENTANA)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            boton_play.manejar_evento(evento)
            boton_exit.manejar_evento(evento)

def pantalla_ganaste():
    def boton_exit_evento():
        pygame.quit()
        exit()

    boton_exit = Boton("assets/exit_button.png", (ANCHO_P_VENTANA // 2, 510), boton_exit_evento)

    while True:
        VENTANA.blit(FONDO_PANTALLA_WINNER, (0, 0))
        boton_exit.dibujar(VENTANA)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            boton_exit.manejar_evento(evento)

def pantalla_perdiste():
    def boton_exit_evento():
        pygame.quit()
        exit()

    boton_exit = Boton("assets/exit_button.png", (ANCHO_P_VENTANA // 2, 510), boton_exit_evento)

    while True:
        VENTANA.blit(FONDO_PANTALLA_GAME_OVER, (0, 0))
        boton_exit.dibujar(VENTANA)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            boton_exit.manejar_evento(evento)

def iniciar_partida(juego_iniciado):
    reloj = pygame.time.Clock()
    juego = Juego(VENTANA)
    prof = 2  

    def boton_back_evento():
        juego_iniciado[0] = False

    boton_back = Boton("assets/back_button.png", (ANCHO_P + 140, 670), boton_back_evento, (193, 70))

    while juego_iniciado[0]:
        reloj.tick(FPS)

        if juego.ganador() is not None:
            if juego.ganador() == NEGRO:
                pantalla_ganaste()
            else:
                pantalla_perdiste()
            juego_iniciado[0] = False

        if juego.turno == BLANCO:
            raiz = Nodo(juego.obtener_tablero(), turno_max=True)
            arbol = Arbol(raiz)

            valor = minimax_nodo(raiz, prof, juego)

            mejor_hijo = max(raiz.hijos, key=lambda n: n.evaluacion)
            juego.mov_ia(mejor_hijo.estado)

            # imprimir el arbol
            arbol.recorrer()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_iniciado[0] = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                if x < 720:
                    fila, columna = obtener_fila_columna_mouse(pos)
                    juego.seleccionar(fila, columna)

            boton_back.manejar_evento(evento)

        juego.actualizar()

def main():
    juego_iniciado = [False]

    while True:
        pantalla_inicio(juego_iniciado)
        iniciar_partida(juego_iniciado)

main()
