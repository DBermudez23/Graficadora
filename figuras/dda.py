def dda_line(x1, y1, x2, y2, canvas, color):
    """
    Dibuja una línea entre (x1, y1) y (x2, y2) sobre el canvas usando el algoritmo DDA.
    
    :param x1: Coordenada x del punto inicial
    :param y1: Coordenada y del punto inicial
    :param x2: Coordenada x del punto final
    :param y2: Coordenada y del punto final
    :param canvas: Instancia de Canvas donde se va a dibujar
    :param color: Color de la línea
    """
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))  # número de pasos necesarios

    if steps == 0:
        canvas.put_pixel(round(x1), round(y1), color)
        return

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        canvas.put_pixel(round(x), round(y), color)
        x += x_inc
        y += y_inc
