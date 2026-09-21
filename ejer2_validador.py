
# EJERCICIO 2


class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self,nota):
        if nota >=0 and nota <= 100:
            return True
        else:
            return False
        #return 0 <= nota <= 100
    
    def cargar_notas(self,*args):
        
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(-60,80,40,200))
print(cal.promedio())






# EJERCICIO 2.1


# EJERCICIO-2.1
# CONTROL DE EDADES

class ControlEdades:
    def __init__(self):
        self.edades = []

    def validar_edad(self, edad):
        if edad >= 1 and edad <= 100:
            return True
        else:
            return False

    def cargar_edades(self, *args):
        for edad in args:
            if self.validar_edad(edad):
                self.edades.append(edad)

        return self.edades

    def promedio(self):
        return sum(self.edades) / len(self.edades)



control = ControlEdades()


print("¿15 es una edad válida?", control.validar_edad(15))
print("¿150 es una edad válida?", control.validar_edad(150))
print("Edades válidas:", control.cargar_edades(-5, 15, 20, 150, 25))
print("Promedio de edades:", control.promedio())

