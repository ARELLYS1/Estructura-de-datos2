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