class Herramientas:
    def __init__(self):
        self.herramienta_activa = "dda"         # Herramienta por defecto
        self.color = (0, 0, 0)                   # Negro
        self.grosor = 1                          # Grosor por defecto (no usado aún)

    def seleccionar(self, nombre):
        """
        Cambia la herramienta activa.
        """
        self.herramienta_activa = nombre.lower()

    def obtener(self):
        """
        Devuelve el nombre de la herramienta activa.
        """
        return self.herramienta_activa  

    def set_color(self, color):
        """
        Establece un nuevo color de dibujo.
        """
        self.color = color

    def get_color(self):
        """
        Retorna el color actual.
        """
        return self.color

    def set_grosor(self, grosor):
        """
        Establece el grosor de trazo (para usos futuros).
        """
        self.grosor = grosor

    def get_grosor(self):
        """
        Obtiene el grosor actual.
        """
        return self.grosor
