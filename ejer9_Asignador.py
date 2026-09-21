# ASIGNADOR DE EQUIPOS 

# Clase Equipos que:
# (1) tenga método crear_equipo(nombre_equipo) 
# que inicie un equipo como una lista vacía en un diccionario;
# (2) tenga método agregar_jugador(equipo, jugador)
# que añada el jugador al equipo;
# (3) tenga método equipo_mayor_integrantes() 
# que retorne el nombre del equipo con más jugadores.

class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = ""
        cantidad = 0

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > cantidad:
                cantidad = len(jugadores)
                mayor = equipo

        return mayor



e = Equipos()


e.crear_equipo("Barcelona")
e.crear_equipo("Emelec")


e.agregar_jugador("Barcelona", "Juan")
e.agregar_jugador("Barcelona", "Pedro")
e.agregar_jugador("Barcelona", "Carlos")

e.agregar_jugador("Emelec", "Luis")
e.agregar_jugador("Emelec", "Miguel")


print(e.equipo_mayor_integrantes())



#EJERCICIO9.1
#ASIGNADOR DE CURSOS
# Tenga un método crear_curso(nombre_curso) que cree un curso vacío dentro de un diccionario.
# Tenga un método agregar_estudiante(curso, estudiante) que agregue un estudiante al curso.
# Tenga un método curso_mayor_estudiantes() que retorne el nombre del curso que tenga más estudiantes.


class Cursos:

    def __init__(self):
        self.cursos = {}

    def crear_curso(self, nombre_curso):
        self.cursos[nombre_curso] = []

    def agregar_estudiante(self, curso, estudiante):
        self.cursos[curso].append(estudiante)

    def curso_mayor_estudiantes(self):
        mayor = ""
        cantidad = 0

        for curso, estudiantes in self.cursos.items():
            if len(estudiantes) > cantidad:
                cantidad = len(estudiantes)
                mayor = curso

        return mayor


c = Cursos()

c.crear_curso("Programacion")
c.crear_curso("Matematicas")

c.agregar_estudiante("Programacion", "Ana")
c.agregar_estudiante("Programacion", "Pedro")
c.agregar_estudiante("Programacion", "Luis")

c.agregar_estudiante("Matematicas", "Maria")
c.agregar_estudiante("Matematicas", "Carlos")

print(c.curso_mayor_estudiantes())