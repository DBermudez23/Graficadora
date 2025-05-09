from figuras.raster import draw_symmetric_points

def bresenham_circle(xc, yc, r, canvas, color):
    """
    Dibuja una circunferencia centrada en (xc, yc) con radio r usando el algoritmo de Bresenham.

    :param xc: Centro en x
    :param yc: Centro en y
    :param r: Radio de la circunferencia
    :param canvas: Lienzo donde se dibuja
    :param color: Color de la circunferencia
    """
    x = 0
    y = r
    d = 3 - 2 * r  # decisión inicial

    while x <= y:
        draw_symmetric_points(canvas, xc, yc, x, y, color)
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1


def bresenham_line(x1, y1, x2, y2, canvas, color=(0, 0, 0)):
    """
    Dibuja una línea entre (x1, y1) y (x2, y2) usando el algoritmo de Bresenham.
    
    :param x1: Coordenada x del punto inicial
    :param y1: Coordenada y del punto inicial
    :param x2: Coordenada x del punto final
    :param y2: Coordenada y del punto final
    :param canvas: Instancia del lienzo
    :param color: Color de la línea
    """
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dy <= dx:
        err = 2 * dy - dx
        for _ in range(dx):
            canvas.put_pixel(x, y, color)
            if err >= 0:
                y += sy
                err -= 2 * dx
            x += sx
            err += 2 * dy
    else:
        err = 2 * dx - dy
        for _ in range(dy):
            canvas.put_pixel(x, y, color)
            if err >= 0:
                x += sx
                err -= 2 * dy
            y += sy
            err += 2 * dx

    canvas.put_pixel(x2, y2, color)  # último punto
