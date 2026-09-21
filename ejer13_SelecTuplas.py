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






# EJERCICIO 13.1
# FILTRADOR DE NÚMEROS CON TUPLAS

# Clase FiltradorNumeros que:
# (1) tenga método crear_rango(inicio, fin)
# que retorne una tupla con los números del rango;
# (2) tenga método combinar_rangos(*rangos)
# que reciba múltiples tuplas (inicio, fin) y retorne una
# lista combinada sin números duplicados usando un conjunto;
# (3) tenga método numeros_pares(rango)
# que reciba una tupla (inicio, fin) y retorne una lista
# con solamente los números pares del rango. 



# FILTRADOR DE NÚMEROS CON TUPLAS

class FiltradorNumeros:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def combinar_rangos(self, *rangos):
        numeros = set()

        for rango in rangos:
            inicio, fin = rango
            for numero in range(inicio, fin + 1):
                numeros.add(numero)

        return list(numeros)

    def numeros_pares(self, rango):
        inicio, fin = rango
        pares = []

        for numero in range(inicio, fin + 1):
            if numero % 2 == 0:
                pares.append(numero)

        return pares



filtrador = FiltradorNumeros()


rango1 = filtrador.crear_rango(1, 5)
rango2 = filtrador.crear_rango(4, 8)


print("Rango 1:", rango1)
print("Rango 2:", rango2)

print("Rangos combinados:", 
      filtrador.combinar_rangos((1, 5), (4, 8)))

print("Números pares:", 
      filtrador.numeros_pares((1, 10)))

