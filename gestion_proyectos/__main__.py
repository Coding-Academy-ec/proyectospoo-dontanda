# Autor:
#        Diego F. Tandazo Yaguachi
#        2024

from gestion_proyectos.equipos.equipo import Equipo
from gestion_proyectos.proyectos.proyecto import Proyecto
from gestion_proyectos.tareas.tarea import Tarea
from gestion_proyectos.tareas.tareaproyecto import TareaProyecto

def main():
    equipo1 = Equipo("Equipo de ingenieros civiles y arquitectos", 5)
    equipo2 = Equipo("Equipo de tecnicos informáticos", 3 )
    equipo3 = Equipo("Equipo de programadores", 4 )
    
    proyecto1 = Proyecto("Contruccion de una casa", 52000)
    proyecto2 = Proyecto("Ensamblado de una computadora de escritorio", 950)
    proyecto3 = Proyecto("Contruccion de un portal web", 1400)
    
    fecha_limite1_1 = "2024-05-10"
    fecha_limite2_1 = "2024-06-01"
    tarea1_1 = Tarea("Estudio de suelo", "Inspección del terreno, toma de muestras, analisis y redaccion del informe", fecha_limite1_1)
    tarea2_1 = Tarea("Levantamiento topografico", "Toma de medidas, digitalización e informes", fecha_limite2_1)

    fecha_limite1_2 = "2024-04-20"
    fecha_limite2_2 = "2024-04-30"
    tarea1_2 = Tarea("Cotización", "Selección de componentes tecnologicos de vanguardia y analisis de costos", fecha_limite1_2)
    tarea2_2 = Tarea("Capacitación", "Personal técnico será capacitado en técnicas de configuración del nuevo hardware", fecha_limite2_2)

    fecha_limite1_3 = "2024-04-25"
    fecha_limite2_3 = "2024-05-10"
    tarea1_3 = Tarea("Requerimientos", "Recopilación de requerimientos", fecha_limite1_3)
    tarea2_3 = Tarea("Análisis y diseño", "Filtrado de requerimientos y maquetación de modulos", fecha_limite2_3)

    tarea_proyecto1_1 = TareaProyecto( tarea1_1, proyecto1, equipo1 )
    tarea_proyecto1_1.registrar()
    tarea_proyecto2_1 = TareaProyecto( tarea2_1, proyecto1, equipo1 )
    tarea_proyecto2_1.registrar()
    
    tarea_proyecto1_2 = TareaProyecto( tarea1_2, proyecto2, equipo2 )
    tarea_proyecto1_2.registrar()
    tarea_proyecto2_2 = TareaProyecto( tarea2_2, proyecto2, equipo2 )
    tarea_proyecto2_2.registrar()

    tarea_proyecto1_3 = TareaProyecto( tarea1_3, proyecto3, equipo3 )
    tarea_proyecto1_3.registrar()
    tarea_proyecto2_3 = TareaProyecto( tarea2_3, proyecto3, equipo3 )
    tarea_proyecto2_3.registrar()
    
    print("\nTareas del proyecto 1: " + proyecto1.__str__())
    print( tarea_proyecto1_1 )
    print( tarea_proyecto2_1 )

    print("\nTareas del proyecto 2: " + proyecto2.__str__())
    print( tarea_proyecto1_2 )
    print( tarea_proyecto2_2 )

    print("\nTareas del proyecto 3: " + proyecto3.__str__())
    print( tarea_proyecto1_3 )
    print( tarea_proyecto2_3 )
    
if __name__ == "__main__":
    main()