# GRUPO DE EDADES 

# Clase AgrupadorEdades que:
# (1) tenga método clasificar_edad(edad) que retorne la categoría 
# ("niño", "adolescente", "adulto", "mayor"); 
# (2) tenga método agrupar_por_categoria(*edades) 
# que retorne un diccionario con {categoría: [edades]};
# (3) tenga método edad_promedio_categoria(categoria).



class AgrupadorEdades:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos[categoria]

        if len(edades) == 0:
            return 0

        return sum(edades) / len(edades)


ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(5, 17, 30, 90))

print(ae.edad_promedio_categoria("adulto"))





# ejercicio 18.1
# Clase AgrupadorNotas que:
# (1) tenga método clasificar_nota(nota) que retorne la categoría
# ("reprobado", "regular", "bueno", "excelente");
# (2) tenga método agrupar_por_categoria(*notas)
# que retorne un diccionario con {categoría: [notas]};
# (3) tenga método promedio_categoria(categoria)
# que retorne el promedio de las notas de esa categoría;
# (4) tenga método nota_mayor_categoria(categoria)
# que retorne la nota más alta de una categoría.


class AgrupadorNotas:

    def __init__(self):
        self.notas = {
            "reprobado": [],
            "regular": [],
            "bueno": [],
            "excelente": []
        }

    def clasificar_nota(self, nota):
        if nota < 6:
            return "reprobado"
        elif nota < 8:
            return "regular"
        elif nota < 9:
            return "bueno"
        else:
            return "excelente"

    def agrupar_por_categoria(self, *notas):
   
        for categoria in self.notas:
            self.notas[categoria] = []

        for nota in notas:
            categoria = self.clasificar_nota(nota)
            self.notas[categoria].append(nota)

        return self.notas

    def promedio_categoria(self, categoria):
        lista = self.notas[categoria]

        if len(lista) == 0:
            return 0

        return sum(lista) / len(lista)

    def nota_mayor_categoria(self, categoria):
        lista = self.notas[categoria]

        if len(lista) == 0:
            return None

        return max(lista)



agrupador = AgrupadorNotas()


print(agrupador.agrupar_por_categoria(
    5, 7, 8, 9, 10, 6, 8.5
))


print("Categoría de 9:", agrupador.clasificar_nota(9))


print("Promedio de bueno:",
      agrupador.promedio_categoria("bueno"))

print("Nota mayor de excelente:",
      agrupador.nota_mayor_categoria("excelente"))

