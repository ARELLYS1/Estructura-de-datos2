# MATRIZ DE DISTANCIAS 

#Clase CalculadorDistancia que:
# (1) tenga método distancia_euclidiana(p1, p2)
# que reciba dos tuplas (x,y)y calcule la distancia; 
# (2) tenga método punto_mas_cercano(referencia, *puntos) 
# que retorne el punto más cercano a referencia;
# (3) tenga un atributo lista para guardar todas 
# las distancias calculadas.


import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        menor_distancia = float("inf")

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < menor_distancia:
                menor_distancia = distancia
                punto_cercano = punto

        return punto_cercano


cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))

print(cd.punto_mas_cercano((0, 0), (3, 4), (1, 1), (5, 2)))

print(cd.distancias)





# EJERCICIO 19.1
# CALCULADOR DE ÁREAS

# Clase CalculadorArea que:
# (1) tenga método area_rectangulo(base, altura)
# que reciba la base y altura y calcule el área;
# (2) tenga método area_mayor(*rectangulos)
# que reciba varias tuplas (base, altura) y retorne
# el rectángulo con mayor área;
# (3) tenga un atributo lista para guardar todas
# las áreas calculadas;
# (4) tenga método promedio_areas()
# que retorne el promedio de todas las áreas calculadas.


# CALCULADOR DE ÁREAS

class CalculadorArea:

    def __init__(self):
        self.areas = []

    
    def area_rectangulo(self, base, altura):
        area = base * altura
        self.areas.append(area)
        return area


    def area_mayor(self, *rectangulos):
        mayor = None
        area_mayor = 0

        for rectangulo in rectangulos:
            base, altura = rectangulo
            area = self.area_rectangulo(base, altura)

            if area > area_mayor:
                area_mayor = area
                mayor = rectangulo

        return mayor


    def promedio_areas(self):
        if len(self.areas) == 0:
            return 0

        return sum(self.areas) / len(self.areas)



calculador = CalculadorArea()


print("Área del rectángulo:", calculador.area_rectangulo(5, 4))


print("Rectángulo con mayor área:",
      calculador.area_mayor(
          (5, 4),
          (10, 3),
          (6, 6)
      ))


print("Promedio de áreas:", calculador.promedio_areas())

