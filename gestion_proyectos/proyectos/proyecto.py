
class Proyecto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto

    def __str__(self):
        return f"'{self.nombre}', presupuesto $ {self.presupuesto}"