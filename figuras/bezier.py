def bezier_cubic(p0, p1, p2, p3, canvas, color=(0, 0, 0), steps=1000):
    """
    Dibuja una curva de Bézier cúbica con 4 puntos de control usando el algoritmo paramétrico.

    :param p0: Punto inicial (x0, y0)
    :param p1: Primer punto de control
    :param p2: Segundo punto de control
    :param p3: Punto final (x3, y3)
    :param canvas: Lienzo sobre el cual se dibuja
    :param color: Color de la curva
    :param steps: Precisión del trazado (más pasos = curva más suave)
    """
    def interpolate(t, p0, p1, p2, p3):
        # Fórmula cúbica: B(t) = (1−t)^3 * P0 + 3(1−t)^2 * t * P1 + 3(1−t) * t^2 * P2 + t^3 * P3
        x = (1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0]
        y = (1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
        return round(x), round(y)

    previous_point = p0
    for i in range(1, steps + 1):
        t = i / steps
        current_point = interpolate(t, p0, p1, p2, p3)
        canvas.put_pixel(*current_point, color)
        previous_point = current_point
