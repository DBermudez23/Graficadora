import pygame
import pygame_gui
from canvas import Canvas
from herramientas import Herramientas
from interfaz.gui import crear_botones, crear_paleta_colores
from interfaz.eventos import manejar_eventos_mouse

# Inicialización
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graficador 2D")

# Inicialización del UI manager
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
botones = crear_botones(manager)
botones_colores = crear_paleta_colores(manager, y=50)

# Instancias del lienzo y herramientas
canvas = Canvas(WIDTH, HEIGHT - 100)
herramientas = Herramientas()

# Lista de puntos para figuras
puntos = []

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        manager.process_events(event) # Procesar eventos de pygame_gui para usar event.ui_element (PyGame)
        if event.type == pygame.QUIT:
            running = False

        # Detectar clics en botones y cambiar herramienta activa
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for nombre, boton in botones.items():
                if event.ui_element == boton:
                    if nombre == "limpiar":
                        canvas.clear()
                        puntos.clear()
                    else:
                        herramientas.seleccionar(nombre)
                        puntos.clear()
            # Colores
            for nombre, boton in botones_colores.items():
                if event.ui_element == boton:
                    herramientas.set_color(boton.colores_rgb)

        # Capturar clics sobre el canvas
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[1] > 70:  # evitar barra superior
                puntos = manejar_eventos_mouse(
                    event=type("Click", (), {"pos": event.pos, "type": "click"}),
                    herramienta_activa=herramientas.obtener(),
                    puntos=puntos,
                    canvas=canvas
                )

        manager.process_events(event)

    # Renderizado
    manager.update(time_delta)
    screen.fill((100, 100, 100))  # fondo gris claro
    canvas.blit_to(screen, (0, 100))  # espacio para barra superior
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
