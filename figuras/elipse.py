def midpoint_ellipse(xc, yc, rx, ry, canvas, color):
    """
    Dibuja una elipse centrada en (xc, yc) con radios rx y ry usando el algoritmo del punto medio.

    :param xc: Coordenada x del centro
    :param yc: Coordenada y del centro
    :param rx: Radio horizontal
    :param ry: Radio vertical
    :param canvas: Instancia del lienzo donde se va a dibujar
    :param color: Color del trazo
    """
    x = 0
    y = ry

    # Región 1
    rx2 = rx * rx
    ry2 = ry * ry
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2
    px = 0
    py = two_rx2 * y

    # Decisión inicial
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    while px < py:
        plot_ellipse_points(canvas, xc, yc, x, y, color)
        x += 1
        px += two_ry2
        if p1 < 0:
            p1 += ry2 + px
        else:
            y -= 1
            py -= two_rx2
            p1 += ry2 + px - py

    # Región 2
    p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2
    while y >= 0:
        plot_ellipse_points(canvas, xc, yc, x, y, color)
        y -= 1
        py -= two_rx2
        if p2 > 0:
            p2 += rx2 - py
        else:
            x += 1
            px += two_ry2
            p2 += rx2 - py + px

def plot_ellipse_points(canvas, xc, yc, x, y, color):
    """
    Dibuja los 4 puntos simétricos de la elipse desde el centro (xc, yc).
    """
    canvas.put_pixel(xc + x, yc + y, color)
    canvas.put_pixel(xc - x, yc + y, color)
    canvas.put_pixel(xc + x, yc - y, color)
    canvas.put_pixel(xc - x, yc - y, color)
    