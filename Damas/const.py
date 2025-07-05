import pygame

pygame.init()

ANCHO_P_VENTANA, ALTO_P_VENTANA = 990, 720
ANCHO_P, ALTO_P = 720, 720
FILAS, COLUMNAS = 8, 8
TAM_CASILLERO = ANCHO_P//COLUMNAS

# Color de fichas
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0) 

# Color de tablero
MARRON = (204, 102, 0)
NARANJA = (255, 204, 153)

# Color de la selección
CELESTE = (153, 255, 255)

# Panel
COLOR_PANEL = (114, 50, 28)
COLOR_TEXTO = (255, 255, 255)
FUENTE_TEXTO = pygame.font.Font("assets/Savate.ttf",22)
FUENTE_TITULO = pygame.font.Font("assets/BitcountGridDouble.ttf",36)

# Pantalla principal
FUENTE_PANTALLA_PRINCIPAL = pygame.font.Font("assets/BitcountGridDouble.ttf", 300)

CORONA = pygame.transform.scale(pygame.image.load('assets/corona.png'), (44, 25))
TITULO_PANEL = pygame.transform.scale(pygame.image.load('assets/titulo_panel.png'), (193, 70))
FONDO_PANTALLA = pygame.transform.scale(pygame.image.load('assets/fondo_pantalla.jpg'), (990, 720))
BOTON_EXIT = pygame.transform.scale(pygame.image.load('assets/exit_button.png'), (193, 70))
BOTON_BACK = pygame.transform.scale(pygame.image.load('assets/back_button.png'), (193, 70))
FONDO_PANTALLA_WINNER = pygame.transform.scale(pygame.image.load('assets/fondo_winner.jpg'), (990, 720))
FONDO_PANTALLA_GAME_OVER = pygame.transform.scale(pygame.image.load('assets/fondo_game_over.jpg'), (990, 720))
