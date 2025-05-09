"""
Funciones comunes para el trazado de gráficos rasterizados.
"""

def put_pixel_safe(canvas, x, y, color):
    """
    Coloca un píxel en el lienzo si está dentro de los límites válidos.
    """
    if 0 <= x < canvas.width and 0 <= y < canvas.height:
        canvas.put_pixel(x, y, color)


def draw_symmetric_points(canvas, xc, yc, x, y, color=(0, 0, 0)):
    """
    Dibuja los 8 puntos simétricos de un círculo alrededor del centro (xc, yc).
    Útil para Bresenham de circunferencias.
    """
    put_pixel_safe(canvas, xc + x, yc + y, color)
    put_pixel_safe(canvas, xc - x, yc + y, color)
    put_pixel_safe(canvas, xc + x, yc - y, color)
    put_pixel_safe(canvas, xc - x, yc - y, color)
    put_pixel_safe(canvas, xc + y, yc + x, color)
    put_pixel_safe(canvas, xc - y, yc + x, color)
    put_pixel_safe(canvas, xc + y, yc - x, color)
    put_pixel_safe(canvas, xc - y, yc - x, color)


def draw_cross(canvas, x, y, size=2, color=(255, 0, 0)):
    """
    Dibuja una cruz pequeña centrada en (x, y). Útil para marcar puntos de control.
    """
    for dx in range(-size, size + 1):
        put_pixel_safe(canvas, x + dx, y, color)
    for dy in range(-size, size + 1):
        put_pixel_safe(canvas, x, y + dy, color)


def lerp(p0, p1, t):
    """
    Interpolación lineal entre dos puntos p0 y p1. Útil para curvas o animaciones.
    """
    return (
        (1 - t) * p0[0] + t * p1[0],
        (1 - t) * p0[1] + t * p1[1]
    )
