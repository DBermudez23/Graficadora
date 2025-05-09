from figuras.dda import dda_line
from figuras.bresenham import bresenham_line, bresenham_circle
from figuras.bezier import bezier_cubic
from figuras.elipse import midpoint_ellipse
from figuras.poligonos import draw_polygon
from herramientas import Herramientas
from figuras.raster import draw_cross  # ayuda visual para puntos

herramientas = Herramientas()

def manejar_eventos_mouse(event, herramienta_activa, puntos, canvas):
    """
    Captura clics del mouse y ejecuta la herramienta activa.
    
    :param event: Evento PyGame transformado (solo tipo "click" con .pos)
    :param herramienta_activa: str con el nombre de la herramienta
    :param puntos: lista actual de puntos [(x, y)]
    :param canvas: instancia del Canvas
    :return: lista actualizada de puntos
    """
    if event.type == "click":
        offset_y = 100  # altura del área superior (barra de herramientas)
        x = round(event.pos[0])
        y = round(event.pos[1] - offset_y)

        if y > 70:  # evitar la barra de herramientas
            puntos.append((x, y))

            # Marcar el punto visualmente
            draw_cross(canvas, x, y, color=herramientas.get_color())

            # Figuras con 2 puntos
            if herramienta_activa in ("dda", "bresenham", "circunferencia", "elipse") and len(puntos) == 2:
                x1, y1 = puntos[0]
                x2, y2 = puntos[1]

                if herramienta_activa == "dda":
                    dda_line(x1, y1, x2, y2, canvas, color=herramientas.get_color())

                elif herramienta_activa == "bresenham":
                    bresenham_line(x1, y1, x2, y2, canvas, color=herramientas.get_color())

                elif herramienta_activa == "circunferencia":
                    r = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                    bresenham_circle(x1, y1, r, canvas, color=herramientas.get_color())

                elif herramienta_activa == "elipse":
                    rx = abs(x2 - x1)
                    ry = abs(y2 - y1)
                    midpoint_ellipse(x1, y1, rx, ry, canvas, color=herramientas.get_color())

                puntos = []

            # Bézier cúbica: 4 puntos
            elif herramienta_activa == "bézier" and len(puntos) == 4:
                bezier_cubic(puntos[0], puntos[1], puntos[2], puntos[3], canvas, color=herramientas.get_color())
                puntos = []

            # Polígonos (triángulo, rectángulo, etc.)
            elif herramienta_activa in ("triángulo", "rectángulo", "polígono") and len(puntos) >= 3:
                if herramienta_activa != "polígono" or len(puntos) == 5: 
                    draw_polygon(puntos, canvas, color=herramientas.get_color())
                    puntos = []

    return puntos
