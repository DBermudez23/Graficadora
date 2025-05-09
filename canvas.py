import pygame

class Canvas:
    def __init__(self, width, height, bg_color=(255, 255, 255)):
        """
        Inicializa un lienzo en blanco donde se puede dibujar píxel a píxel.
        """
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.surface = pygame.Surface((width, height))
        self.clear()

    def put_pixel(self, x, y, color):
        """
        Coloca un píxel en la posición (x, y) si está dentro de los límites.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.surface.set_at((x, y), color)

    def get_pixel(self, x, y):
        """
        Retorna el color del píxel en (x, y).
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.surface.get_at((x, y))
        return None

    def clear(self):
        """
        Limpia el lienzo rellenándolo con el color de fondo.
        """
        self.surface.fill(self.bg_color)

    def blit_to(self, target_surface, position=(0, 0)):
        """
        Dibuja este canvas sobre otra superficie (como la ventana principal).
        """
        target_surface.blit(self.surface, position)
