from figuras.bresenham import bresenham_line

def draw_polygon(points, canvas, color):
    """
    Dibuja un polígono cerrando una secuencia de puntos mediante líneas.

    :param points: Lista de tuplas [(x0, y0), (x1, y1), ..., (xn, yn)]
    :param canvas: Instancia del lienzo
    :param color: Color del borde del polígono
    """
    if len(points) < 2:
        return  # No se puede construir un polígono

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        bresenham_line(x1, y1, x2, y2, canvas, color)

    # Cerrar el polígono: conectar el último punto con el primero
    x1, y1 = points[-1]
    x2, y2 = points[0]
    bresenham_line(x1, y1, x2, y2, canvas, color)
