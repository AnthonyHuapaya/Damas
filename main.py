import pygame
from Damas.const import ANCHO_P_VENTANA, ALTO_P_VENTANA, TAM_CASILLERO, NEGRO, BLANCO, FUENTE_PANTALLA_PRINCIPAL, FONDO_PANTALLA, ANCHO_P, FONDO_PANTALLA_WINNER, FONDO_PANTALLA_GAME_OVER
from Damas.juego import Juego
from minimax.Algoritmo import minimax
from Damas.boton import Boton

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

def main():
    juego_iniciado = [False]
    programa_levantado = True

    while programa_levantado:
        pantalla_inicio(juego_iniciado)
        iniciar_partida(juego_iniciado)


main()

