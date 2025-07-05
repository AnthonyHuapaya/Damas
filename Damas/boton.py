import pygame

class Boton:
    def __init__(self, imagen, pos, accion = None, tam = None):
        imagen_original = pygame.image.load(imagen).convert_alpha()
        if tam:
            self.imagen = pygame.transform.scale(imagen_original, tam)
        else:
            self.imagen = imagen_original
        
        self.rect = self.imagen.get_rect(center = pos)
        self.accion = accion

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect.topleft)

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                if self.accion:
                    self.accion()