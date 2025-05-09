import pygame
import pygame_gui

def crear_botones(manager):
    """
    Crea botones para las herramientas disponibles del graficador.
    Retorna un diccionario con las referencias.
    """
    botones = {}

    nombres = [
        "DDA", "Bresenham", "Circunferencia", "Bézier",
        "Triángulo", "Rectángulo", "Polígono", "Elipse",
        "Limpiar"
    ]

    for i, nombre in enumerate(nombres):
        botones[nombre.lower()] = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10 + i * 110, 10), (100, 30)),
            text=nombre,
            manager=manager
        )

    return botones

def crear_paleta_colores(manager, y=50):
    """
    Crea botones de color como paleta. Retorna un diccionario {nombre: botón}.
    """
    colores = {
        "negro": (0, 0, 0),
        "rojo": (255, 0, 0),
        "verde": (0, 255, 0),
        "azul": (0, 0, 255),
        "amarillo": (255, 255, 0),
        "magenta": (255, 0, 255),
        "cian": (0, 255, 255)
    }

    botones = {}
    for i, (nombre, rgb) in enumerate(colores.items()):
        botones[nombre] = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10 + i * 60, y), (50, 30)),
            text='',
            manager=manager,
            tool_tip_text=nombre.capitalize()
        )
        botones[nombre].colores_rgb = rgb  # añadimos el color al botón

    return botones
