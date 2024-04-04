class TareaProyecto:
    def __init__(self, tarea, proyecto, equipo):
        self.tarea = tarea
        self.proyecto = proyecto
        self.equipo = equipo
        
    def __str__(self):
        return f"   * {self.tarea.titulo}, asignado a: {self.equipo.nombre}"
        
    def registrar(self):
        # Lógica para registrar la asociacion entre una tarea de un proyecto con el equipo responsable
        pass