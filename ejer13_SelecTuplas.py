#SELECTOR DE RANGO CON TUPLAS 

# Clase SelectorRango que: 
# (1) tenga método crear_rango(inicio, fin)
# que retorne una tupla con números en ese rango;
# (2) tenga método elementos_en_multiples_rangos(*rangos)
# que reciba múltiples tuplas (inicio,fin) y retorne una
# lista combinada sin duplicados usando un conjunto.


class SelectorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()

        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]

            numeros = self.crear_rango(inicio, fin)

            for numero in numeros:
                elementos.add(numero)

        return list(elementos)



sr = SelectorRango()


print(sr.crear_rango(1, 3))


print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))


